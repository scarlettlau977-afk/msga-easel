"""Offline network-policy regression using the existing fake app-server."""
import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

from easel.harnesses.base import RunRequest
from easel.harnesses.codex import CodexAdapter

FIXTURE = Path(__file__).parent / "fixtures" / "harness_rpc.py"


class CodexNetworkPolicyTests(unittest.TestCase):
    def test_project_network_opt_in_preserves_file_and_approval_policy(self):
        for sandbox in ("read-only", "workspace-write"):
            for value, enabled in (
                ("", False), ("false", False), ("invalid", False),
                ("true", True), ("1", True), (" YES ", True), ("on", True),
            ):
                with self.subTest(sandbox=sandbox, value=value):
                    with tempfile.TemporaryDirectory() as directory:
                        cwd = Path(directory)
                        env = {
                            **os.environ,
                            "FAKE_HARNESS_MODE": "stable-resume",
                            "FAKE_HARNESS_AUDIT": str(cwd / "audit.jsonl"),
                            "EASEL_CODEX_NETWORK_ACCESS": value,
                        }
                        request = RunRequest(
                            "offline policy check", cwd, env, sandbox=sandbox,
                            timeout=10,
                            command=(sys.executable, str(FIXTURE), "codex"),
                        )

                        async def reject(questions):
                            raise AssertionError("No approvals expected")

                        asyncio.run(CodexAdapter().run(
                            request, lambda *args: None, reject, lambda _: None,
                        ))
                        messages = [
                            json.loads(line) for line in
                            (cwd / "audit.jsonl").read_text().splitlines()
                        ]
                        turn = next(m for m in messages if m.get("method") == "turn/start")
                        expected = {"type": "readOnly"} if sandbox == "read-only" else {
                            "type": "workspaceWrite",
                            "writableRoots": [str(cwd)],
                            "networkAccess": enabled,
                        }
                        self.assertEqual(turn["params"]["sandboxPolicy"], expected)
                        self.assertEqual(turn["params"]["approvalPolicy"], "on-request")


if __name__ == "__main__":
    unittest.main()
