"""Smoke tests: every example script must run to completion.

TQ cleanup: parametrized per-example test so each script produces its
own pytest node (instead of one assertion-loop combining all examples).
Each test carries AAA markers (TQ002) and asserts exactly one fact
(TQ007); the test name spells out the behaviour under test (TQ003).
"""

import subprocess
import sys
from pathlib import Path

import pytest

_EXAMPLES_DIR = Path(__file__).resolve().parents[2] / "examples"
EXAMPLES = sorted(_EXAMPLES_DIR.glob("*.py"))


def _example_ids(paths):
    return [p.name for p in paths]


def test_examples_directory_contains_at_least_one_script():
    # Arrange
    discovered = EXAMPLES

    # Act
    count = len(discovered)

    # Assert
    assert count > 0, f"no example scripts found in {_EXAMPLES_DIR}"


@pytest.mark.parametrize("example", EXAMPLES, ids=_example_ids(EXAMPLES))
def test_example_script_exits_zero_when_executed(example, tmp_path):
    # Arrange
    cmd = [sys.executable, str(example)]

    # Act
    result = subprocess.run(
        cmd,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=120,
    )

    # Assert
    assert result.returncode == 0, f"{example.name} failed: {result.stderr}"
