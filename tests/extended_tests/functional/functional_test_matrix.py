"""
Functional test matrix definitions.

This module contains the functional_matrix dictionary which defines all functional tests.
"""

from pathlib import Path

# Note: these paths are relative to the repository root.
SCRIPT_DIR = Path("tests") / "extended_tests" / "functional" / "scripts"


def _get_functional_script_path(script_name: str) -> str:
    platform_path = SCRIPT_DIR / script_name
    # Convert to posix (using `/` instead of `\\`) so test workflows can use
    # 'bash' as the shell on Linux and Windows.
    posix_path = platform_path.as_posix()
    return str(posix_path)


# Functional tests will be added in follow-up PRs.
# Example entry format:
#   "test_name": {
#       "job_name": "test_name",
#       "fetch_artifact_args": "--miopen --tests",
#       "timeout_minutes": 30,
#       "test_script": f"python {_get_functional_script_path('test_name.py')}",
#       "platform": ["linux"],
#       "total_shards": 1,
#   },
functional_matrix = {}
