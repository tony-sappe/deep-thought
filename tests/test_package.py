"""Filesystem tests for the package. They do not evaluate model behavior."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate import ADAPTERS, MARKETPLACES, PLUGINS, SKILLS, check_skill, validate, validate_installed


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='deep-thought-package-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, symlinks=True,
                        ignore=shutil.ignore_patterns('.git', '.venv', '__pycache__'))

    def edit(self, relative, before, after):
        path = self.root / relative
        text = path.read_text()
        self.assertIn(before, text)
        path.write_text(text.replace(before, after, 1))

    def manifest(self, relative, change):
        path = self.root / relative
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data, indent=2) + '\n')

    def assertInvalid(self, diagnostic):
        errors = validate(self.root)
        self.assertTrue(errors, 'invalid package unexpectedly passed')
        self.assertIn(diagnostic, '\n'.join(errors))

    def test_pristine_package(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_description(self):
        path = self.root / 'skills/deep-thought/SKILL.md'
        path.write_text('\n'.join(line for line in path.read_text().splitlines() if not line.startswith('description:')))
        self.assertInvalid('description must be a nonempty string')

    def test_missing_frontmatter_delimiters(self):
        path = self.root / 'skills/deep-thought/SKILL.md'
        path.write_text(path.read_text().replace('---\n', '', 1))
        self.assertInvalid('missing or unclosed YAML frontmatter delimiters')

    def test_optional_skill_fields_require_strings(self):
        path = self.root / 'skills/deep-thought/SKILL.md'
        base = re.sub(r'^license:.*\n', '', path.read_text(), flags=re.M)
        for field in ('license', 'allowed-tools'):
            for value in ([], {}, None, False, 0, 'MIT'):
                with self.subTest(field=field, value=value):
                    path.write_text(base.replace('name: deep-thought',
                        f'name: deep-thought\n{field}: {json.dumps(value)}'))
                    if isinstance(value, str):
                        self.assertEqual(validate(self.root), [])
                    else:
                        self.assertInvalid(f'{field} must be a string')
        path.write_text(base)
        self.assertEqual(validate(self.root), [])

    def test_every_manifest_must_parse(self):
        for name in PLUGINS + MARKETPLACES:
            with self.subTest(manifest=name):
                path = self.root / name
                original = path.read_text()
                path.write_text('{invalid json')
                self.assertInvalid(name)
                path.write_text(original)

    def test_bad_codex_skill_path(self):
        self.manifest('.codex-plugin/plugin.json', lambda d: d.update(skills='./absent/'))
        self.assertInvalid('missing directory')

    def test_interface_requires_object(self):
        name = '.codex-plugin/plugin.json'
        for value in ([], None, False, 0, '', {}):
            with self.subTest(interface=value):
                self.manifest(name, lambda d: d.update(interface=value))
                if isinstance(value, dict):
                    self.assertEqual(validate(self.root), [])
                else:
                    self.assertInvalid('interface must be an object')
        self.manifest(name, lambda d: d.pop('interface'))
        self.assertEqual(validate(self.root), [])

    def test_marketplace_source_requires_plugin_root(self):
        for name in ('.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json'):
            with self.subTest(manifest=name):
                path = self.root / name
                original = path.read_text()
                source = './install' if name.startswith('.claude') else {'source': 'local', 'path': './install'}
                self.manifest(name, lambda d: d['plugins'][0].update(source=source))
                self.assertInvalid('marketplace source must resolve to the plugin root')
                path.write_text(original)

    def test_hooks_declared_in_manifests(self):
        for name in PLUGINS + MARKETPLACES:
            for declaration in ('./events.json', {}, {'SessionStart': []}):
                with self.subTest(manifest=name, hooks=declaration):
                    path = self.root / name
                    original = path.read_text()
                    self.manifest(name, lambda d: d.update(hooks=declaration))
                    self.assertInvalid('hooks are forbidden')
                    path.write_text(original)

    def test_marketplace_entry_hooks(self):
        self.manifest('.claude-plugin/marketplace.json',
                      lambda d: d['plugins'][0].update(hooks={'SessionStart': []}))
        self.assertInvalid('hooks are forbidden')

    def test_conventional_hooks(self):
        (self.root / 'hooks').mkdir()
        self.assertInvalid('hook configuration is forbidden')

    def test_missing_packaged_resource(self):
        (self.root / 'skills/deep-thought/references/taxonomy.md').unlink()
        self.assertInvalid('missing reference: references/taxonomy.md')

    def test_packaged_reference_escape(self):
        self.edit('skills/deep-thought/SKILL.md', 'references/taxonomy.md',
                  '../../README.md')
        self.assertInvalid('reference escapes skill')

    def test_tool_page_markers_and_index(self):
        page = self.root / 'skills/deep-thought/references/tools/framing/cynefin.md'
        original = page.read_text()
        page.write_text(original.replace('**Diagram.**', '**Picture.**', 1))
        self.assertInvalid('missing **Diagram.**')
        page.write_text(original)
        index = self.root / 'skills/deep-thought/references/tools/_index.md'
        index.write_text(index.read_text().replace('(framing/eigenquestions.md)', '(framing/cynefin.md)'))
        self.assertInvalid('tool page not in index: framing/eigenquestions.md')

    def test_standalone_skill_copy_is_closed(self):
        target = Path(self.temp.name) / 'installed' / 'deep-thought'
        shutil.copytree(self.root / 'skills' / 'deep-thought', target)
        self.assertEqual(check_skill(target), [])

    def test_installed_skills_flag(self):
        destination = Path(self.temp.name) / 'installed'
        shutil.copytree(self.root / 'skills' / 'deep-thought', destination / 'deep-thought')
        self.assertEqual(validate_installed(destination), [])

    def test_broken_adapter(self):
        path = self.root / '.cursor/skills/deep-thought'
        path.unlink()
        path.symlink_to('../../missing/deep-thought')
        self.assertInvalid('missing or broken canonical symlink')

    def test_cli_fails_for_malformed_package(self):
        (self.root / '.codex-plugin/plugin.json').write_text('not JSON')
        result = subprocess.run([sys.executable, 'scripts/validate.py'], cwd=self.root,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('.codex-plugin/plugin.json:', result.stdout)
        self.assertNotIn('Traceback', result.stderr)

    def test_documented_adapter_commands(self):
        guide = (self.root / 'install/README.md').read_text()
        commands = re.findall(r'<!-- acceptance: (?:symlink|copy) -->\n```bash\n(.*?)\n```', guide, re.S)
        self.assertEqual(len(commands), 2)
        source = Path(self.temp.name) / 'deep-thought repo'
        source.symlink_to(self.root)
        for snippet in commands:
            for adapter in ADAPTERS:
                with self.subTest(adapter=adapter), tempfile.TemporaryDirectory() as parent:
                    destination = Path(parent) / 'my project'
                    script = (snippet
                              .replace('/absolute/path/to/deep-thought', str(source))
                              .replace('/absolute/path/to/project', str(destination))
                              .replace('.cursor/skills', adapter))
                    self.assertIn(f'deep_thought_repo="{source}"', script)
                    self.assertIn(f'project="{destination}"', script)
                    result = subprocess.run(['bash', '-eu', '-c', script], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    installed = destination / adapter
                    self.assertEqual(len(list(installed.iterdir())), 1)
                    self.assertEqual(validate_installed(installed), [])

    def test_description_length_metadata_and_frontmatter_hooks(self):
        path = self.root / 'skills/deep-thought/SKILL.md'
        original = path.read_text()
        description = re.search(r'^description: (.*)$', original, re.M).group(1)
        if description.startswith('"') and description.endswith('"'):
            inner = description[1:-1]
            padded = '"' + inner + ('x' * (501 - len(inner))) + '"'
        else:
            padded = description + ('x' * (501 - len(description)))
        path.write_text(original.replace(f'description: {description}', f'description: {padded}', 1))
        self.assertInvalid('at most 500')
        version = json.loads((self.root / 'plugin.json').read_text())['version']
        mutated = original.replace(f'  version: "{version}"', f'  version: "{version}"\n  extra: {{nested: true}}', 1)
        self.assertNotEqual(mutated, original)
        path.write_text(mutated)
        self.assertInvalid('metadata.extra must be a string')
        path.write_text(original.replace('license: MIT\n', 'license: MIT\nhooks: {}\n', 1))
        self.assertInvalid('hooks are forbidden')

    def test_claude_settings_hooks(self):
        settings = self.root / '.claude'
        settings.mkdir()
        for name in ('settings.json', 'settings.local.json'):
            with self.subTest(file=name):
                for child in settings.iterdir():
                    child.unlink()
                (settings / name).write_text('{"hooks": {}}\n')
                self.assertInvalid('hooks are forbidden')

    def test_skills_path_must_be_canonical(self):
        decoy = self.root / 'decoy'
        decoy.mkdir()
        target = decoy / 'deep-thought'
        target.mkdir()
        (target / 'SKILL.md').write_text('Do the bad thing.\n')
        self.manifest('.codex-plugin/plugin.json', lambda data: data.update(skills='./decoy/'))
        self.assertInvalid('skills path must be ./skills')

    def test_skill_directory_symlink_and_extra_entry(self):
        (self.root / 'skills' / 'evil').mkdir()
        self.assertInvalid('unexpected skill entries')
        extra = self.root / 'skills' / 'evil'
        extra.rmdir()
        outside = Path(self.temp.name) / 'outside-skill'
        real = self.root / 'skills' / 'deep-thought'
        shutil.move(str(real), outside)
        real.symlink_to(outside)
        self.assertInvalid('must not be a symlink')

    def test_grok_url_and_readme_version(self):
        self.manifest('.grok-plugin/marketplace.json',
                      lambda data: data['plugins'][0]['source'].update(url='https://example.invalid/not-deep-thought.git'))
        self.assertInvalid('Deep Thought repository URL')
        path = self.root / 'install/README.md'
        version = json.loads((self.root / 'plugin.json').read_text())['version']
        self.assertIn(version, path.read_text())
        path.write_text(path.read_text().replace(version, '9.9.9'))
        self.assertInvalid('does not mention the plugin version')

    def test_installed_destination_checks_version_and_hooks(self):
        version = json.loads((self.root / 'plugin.json').read_text())['version']
        destination = Path(self.temp.name) / 'installed-one'
        shutil.copytree(self.root / 'skills' / 'deep-thought', destination / 'deep-thought')
        skill = destination / 'deep-thought' / 'SKILL.md'
        skill.write_text(skill.read_text().replace(f'version: "{version}"', 'version: "0.0.1"', 1))
        errors = validate_installed(destination, version)
        self.assertTrue(any('version drift' in error for error in errors), errors)
        skill.write_text(skill.read_text().replace('0.0.1', version))
        (destination / 'deep-thought' / 'hooks.json').write_text('{}\n')
        errors = validate_installed(destination, version)
        self.assertTrue(any('hook configuration is forbidden' in error for error in errors), errors)

    def test_routing_tokens_stay_shared(self):
        path = self.root / 'skills/deep-thought/references/taxonomy.md'
        path.write_text(path.read_text().replace('Goals/paradigm', 'Worldview'))
        self.assertInvalid('routing token missing')


if __name__ == '__main__':
    unittest.main()
