import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from generate import generate, validate

SOURCE = Path(__file__).resolve().parents[1] / 'global.json'

class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.root.joinpath('global.json').write_bytes(SOURCE.read_bytes())
        self.data = json.loads(SOURCE.read_bytes())

    def test_deterministic_global_only_distribution(self):
        generate(self.root)
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        generate(self.root)
        self.assertEqual(before, {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        manifest = json.loads(self.root.joinpath('manifest.json').read_bytes())
        self.assertNotIn('sites', manifest)
        self.assertFalse(self.root.joinpath('sites').exists())
        record = manifest['global']
        raw = self.root.joinpath(record['path']).read_bytes()
        self.assertEqual(raw, SOURCE.read_bytes())
        self.assertEqual(record['sha256'], hashlib.sha256(raw).hexdigest())
        self.assertEqual(record['size'], len(raw))
        self.assertIn('/rules-v' + str(self.data['code']) + '/', record['url'])
        readme = self.root.joinpath('README.md').read_text()
        for site in self.data['sites']:
            self.assertIn('`' + site['id'] + '`', readme)
        self.assertNotIn('(sites/', readme)

    def test_check_rejects_drift_and_stale_files(self):
        generate(self.root)
        generate(self.root, check=True)
        self.root.joinpath('sites').mkdir()
        self.root.joinpath('sites/stale.json').write_text('{}')
        with self.assertRaises(ValueError): generate(self.root, check=True)
        generate(self.root)
        self.assertFalse(self.root.joinpath('sites/stale.json').exists())
        self.root.joinpath('README.md').write_text('changed')
        with self.assertRaises(ValueError): generate(self.root, check=True)

    def test_invalid_metadata_identity_and_dependency(self):
        mutations = [
            lambda d: d.update(schemaVersion=2),
            lambda d: d.update(code=True),
            lambda d: d['sites'][0].update(id='../escape'),
            lambda d: d['sites'].append(copy.deepcopy(d['sites'][0])),
            lambda d: d['sites'][1].update(domains=d['sites'][0]['domains']),
            lambda d: d['sites'][0].update(architecture='missing'),
            lambda d: d['sites'][0].update(base={'minCode': 9999}),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                d = copy.deepcopy(self.data)
                mutate(d)
                with self.assertRaises(ValueError): validate(d)

if __name__ == '__main__': unittest.main()
