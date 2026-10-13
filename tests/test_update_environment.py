"""Public release helpers must not inherit credentials into child processes."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HELPER = Path(__file__).resolve().parents[1] / 'plugins/reflection-companion/skills/reflection-companion/scripts/updates.py'
spec = importlib.util.spec_from_file_location('updates', HELPER)
updates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updates)


class UpdateEnvironmentTest(unittest.TestCase):
    def test_public_plugin_command_does_not_forward_credentials(self):
        install = updates.CodexInstall(Path('/tmp').resolve() / 'fictional-codex-home')
        with patch.dict(updates.os.environ, {
            'PATH': '/fake/path', 'OPENAI_API_KEY': 'fictional-openai-token',
            'GH_TOKEN': 'fictional-github-token', 'UNRELATED_SECRET': 'fictional-secret',
        }, clear=True), patch.object(updates.shutil, 'which', return_value='/fake/codex'), \
                patch.object(updates.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='{}')) as run:
            self.assertEqual(install.run('marketplace', 'upgrade', updates.NAME), {})
        self.assertEqual(run.call_args.args[0][0], '/fake/codex')
        child = run.call_args.kwargs['env']
        self.assertEqual(set(child), {'PATH', 'CODEX_HOME', 'DISABLE_TELEMETRY', 'DO_NOT_TRACK'})
        self.assertEqual(child['CODEX_HOME'], str(install.home))
        self.assertNotIn('fictional', '\n'.join(v for k, v in child.items() if k != 'CODEX_HOME'))


if __name__ == '__main__':
    unittest.main()
