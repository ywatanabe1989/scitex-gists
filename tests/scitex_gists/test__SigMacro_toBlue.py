#!/usr/bin/env python3
"""Tests for scitex_gists._SigMacro_toBlue (SigmaPlot macro printer)."""

import pytest

from scitex_gists._SigMacro_toBlue import sigmacro_to_blue


class TestSigmacroToBlue:
    def test_prints_a_macro(self, capsys):
        sigmacro_to_blue()
        captured = capsys.readouterr()
        assert captured.out.strip(), "expected non-empty stdout"

    def test_output_contains_option_explicit(self, capsys):
        sigmacro_to_blue()
        captured = capsys.readouterr()
        assert "Option Explicit" in captured.out

    def test_output_defines_getColor(self, capsys):
        sigmacro_to_blue()
        captured = capsys.readouterr()
        assert "Function getColor" in captured.out

    def test_output_includes_blue_rgb(self, capsys):
        sigmacro_to_blue()
        captured = capsys.readouterr()
        assert "RGB(0, 128, 192)" in captured.out

    def test_returns_none(self):
        assert sigmacro_to_blue() is None


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
