"""PS303 example mirror stub: ensure ``examples/quickstart.py`` is syntactically valid.

TQ cleanup: each test asserts exactly one fact (TQ007), the test names
spell out the behaviour under test (TQ003), and bodies carry
``# Arrange / # Act / # Assert`` markers (TQ002).
"""

import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_example_file_exists_on_disk():
    # Arrange
    target = EXAMPLE

    # Act
    exists = target.exists()

    # Assert
    assert exists, f"missing example: {target}"


def test_quickstart_example_compiles_without_syntax_errors():
    # Arrange
    cmd = [sys.executable, "-m", "py_compile", str(EXAMPLE)]

    # Act
    proc = subprocess.run(cmd, capture_output=True, text=True)

    # Assert
    assert proc.returncode == 0, f"py_compile failed: {proc.stderr}"
