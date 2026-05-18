#!/usr/bin/env python3
"""Tests for ``scitex_gists._SigMacro_toBlue`` (SigmaPlot macro printer).

TQ cleanup: docstring states intent (TQ001), each test carries the
``# Arrange / # Act / # Assert`` markers (TQ002), test names spell out
the behaviour under test (TQ003), and every test asserts exactly one
fact (TQ007). Capture relies on the pytest-builtin ``capsys`` — no
mocks, no monkeypatch (PA-306 compliant).
"""

from __future__ import annotations

import pytest

from scitex_gists._SigMacro_toBlue import sigmacro_to_blue


def test_sigmacro_to_blue_prints_non_empty_stdout(capsys):
    # Arrange
    # (nothing to set up beyond capsys auto-fixture)

    # Act
    sigmacro_to_blue()

    # Assert
    assert capsys.readouterr().out.strip() != ""


def test_sigmacro_to_blue_output_contains_option_explicit(capsys):
    # Arrange
    # (capsys auto-fixture only)

    # Act
    sigmacro_to_blue()

    # Assert
    assert "Option Explicit" in capsys.readouterr().out


def test_sigmacro_to_blue_output_defines_get_color_function(capsys):
    # Arrange
    # (capsys auto-fixture only)

    # Act
    sigmacro_to_blue()

    # Assert
    assert "Function getColor" in capsys.readouterr().out


def test_sigmacro_to_blue_output_includes_blue_rgb_triplet(capsys):
    # Arrange
    # (capsys auto-fixture only)

    # Act
    sigmacro_to_blue()

    # Assert
    assert "RGB(0, 128, 192)" in capsys.readouterr().out


def test_sigmacro_to_blue_returns_none_when_called_directly():
    # Arrange
    # (no external state to seed)

    # Act
    result = sigmacro_to_blue()

    # Assert
    assert result is None


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
