#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for ``scitex_gists._SigMacro_processFigure_S``.

PA-306: no ``unittest.mock`` and no ``monkeypatch``. ``sys.stdout`` is
swapped to an in-memory buffer via a tiny ``_swap_stdout`` context
manager with explicit save/restore — same shape as the
scitex-agent-container test helpers.

TQ cleanup: module docstring states intent (TQ001), each test carries
``# Arrange / # Act / # Assert`` markers (TQ002), test names spell out
the property being verified (TQ003), and every test asserts exactly one
fact (TQ007). Same-shape membership checks fan out via
``pytest.parametrize`` so each case is its own pytest node.
"""

from __future__ import annotations

import re
import sys
import warnings
from contextlib import contextmanager
from io import StringIO
from typing import Iterator

import pytest

from scitex_gists import SigMacro_processFigure_S, sigmacro_process_figure_s

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


@contextmanager
def _swap_stdout(buf: StringIO) -> Iterator[StringIO]:
    """Swap ``sys.stdout`` for the duration of the block, then restore."""
    saved = sys.stdout
    sys.stdout = buf
    try:
        yield buf
    finally:
        sys.stdout = saved


def _captured_output() -> str:
    """Run the macro under a swapped stdout and return what it printed."""
    buf = StringIO()
    with _swap_stdout(buf):
        sigmacro_process_figure_s()
    return buf.getvalue()


# ---------------------------------------------------------------------------
# Basic invocation
# ---------------------------------------------------------------------------


def test_sigmacro_process_figure_s_prints_non_empty_output():
    # Arrange
    buf = StringIO()

    # Act
    with _swap_stdout(buf):
        sigmacro_process_figure_s()

    # Assert
    assert buf.getvalue().strip() != ""


def test_sigmacro_process_figure_s_returns_none_when_called():
    # Arrange
    buf = StringIO()

    # Act
    with _swap_stdout(buf):
        result = sigmacro_process_figure_s()

    # Assert
    assert result is None


# ---------------------------------------------------------------------------
# VBA structural elements — one assertion per parametrized case
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "snippet",
    [
        "Option Explicit",
        "Sub Main()",
        "End Sub",
        "Function FlagOn",
        "Function FlagOff",
        "Sub setTitleSize()",
        "Sub setLabelSize(dimension)",
        "Sub setTickLabelSize(dimension)",
        "Sub processTicks(dimension)",
        "Sub removeAxis(dimension)",
        "Sub resizeFigure",
    ],
)
def test_output_contains_vba_structural_snippet(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"VBA snippet not in output: {snippet!r}"


@pytest.mark.parametrize(
    "snippet",
    [
        "Const FLAG_SET_BIT As Long = 1",
        "Const FLAG_CLEAR_BIT As Long = 0",
    ],
)
def test_output_contains_flag_constant_definition(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"flag constant not in output: {snippet!r}"


@pytest.mark.parametrize(
    "snippet",
    [
        "' Constants for FLAG_SET_BIT and FLAG_CLEAR_BIT should be defined",
        "' Function to set option flag bits on",
        "' Function to set option flag bits off",
        "' Procedure to set the title size to 8 points",
        "' Main procedure",
    ],
)
def test_output_contains_explanatory_comment(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"explanatory comment not in output: {snippet!r}"


@pytest.mark.parametrize(
    "snippet",
    [
        '"111"',  # 8-point size token used for title + labels
        '"97"',  # 7-point size token used for tick labels
        "&H000004F5&",  # figure width
        "&H00000378&",  # figure height
    ],
)
def test_output_contains_size_setting_token(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"size setting token not in output: {snippet!r}"


@pytest.mark.parametrize(
    "snippet",
    [
        "setLabelSize(1) ' X-axis",
        "setLabelSize(2) ' Y-axis",
        "setTickLabelSize(1) ' X-axis",
        "setTickLabelSize(2) ' Y-axis",
        "processTicks(1) ' X-axis",
        "processTicks(2) ' Y-axis",
        "removeAxis(1) ' Right axis",
        "removeAxis(2) ' Top axis",
    ],
)
def test_output_contains_axis_operation_call(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"axis-op call not in output: {snippet!r}"


@pytest.mark.parametrize(
    "snippet",
    [
        "ActiveDocument",
        "CurrentPageItem",
        "GraphPages",
        "CurrentPageObject",
        "GPT_GRAPH",
        "GPT_AXIS",
        "SetCurrentObjectAttribute",
    ],
)
def test_output_references_sigmaplot_specific_identifier(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"SigmaPlot identifier not in output: {snippet!r}"


@pytest.mark.parametrize(
    "snippet",
    [
        "Dim FullPATH As String",
        "Dim OrigPageName As String",
        "Dim ObjectType As String",
        "Dim COLOR As Long",
    ],
)
def test_output_contains_dim_declaration(snippet):
    # Arrange
    output = _captured_output()

    # Act
    found = snippet in output

    # Assert
    assert found, f"Dim declaration not in output: {snippet!r}"


# ---------------------------------------------------------------------------
# VBA structural balance
# ---------------------------------------------------------------------------


def test_output_has_balanced_sub_and_end_sub_pairs():
    # Arrange
    output = _captured_output()

    # Act
    sub_count = len(re.findall(r"(?m)^Sub ", output))
    end_sub_count = len(re.findall(r"(?m)^End Sub\b", output))

    # Assert
    assert sub_count == end_sub_count


def test_output_has_balanced_function_and_end_function_pairs():
    # Arrange
    output = _captured_output()

    # Act
    function_count = len(re.findall(r"(?m)^Function ", output))
    end_function_count = len(re.findall(r"(?m)^End Function\b", output))

    # Assert
    assert function_count == end_function_count


def test_output_defines_at_least_seven_sub_procedures():
    # Arrange
    output = _captured_output()

    # Act
    sub_count = len(re.findall(r"(?m)^Sub ", output))

    # Assert
    assert sub_count >= 7


def test_output_spans_many_lines_indicating_full_macro_body():
    # Arrange
    output = _captured_output()

    # Act
    line_count = len(output.strip().split("\n"))

    # Assert
    assert line_count > 50


def test_output_uses_indentation_inside_macro_bodies():
    # Arrange
    output = _captured_output()
    lines = output.strip().split("\n")

    # Act
    indented_line_count = sum(1 for line in lines if line.startswith("    "))

    # Assert
    assert indented_line_count > 0


# ---------------------------------------------------------------------------
# Deprecation wrapper
# ---------------------------------------------------------------------------


def test_deprecated_alias_emits_exactly_one_warning():
    # Arrange
    buf = StringIO()

    # Act
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with _swap_stdout(buf):
            SigMacro_processFigure_S()

    # Assert
    assert len(caught) == 1


def test_deprecated_alias_warning_is_deprecationwarning_category():
    # Arrange
    buf = StringIO()

    # Act
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with _swap_stdout(buf):
            SigMacro_processFigure_S()

    # Assert
    assert issubclass(caught[0].category, DeprecationWarning)


def test_deprecated_alias_warning_message_mentions_old_name():
    # Arrange
    buf = StringIO()

    # Act
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with _swap_stdout(buf):
            SigMacro_processFigure_S()

    # Assert
    assert "SigMacro_processFigure_S is deprecated" in str(caught[0].message)


def test_deprecated_alias_warning_message_points_to_new_name():
    # Arrange
    buf = StringIO()

    # Act
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with _swap_stdout(buf):
            SigMacro_processFigure_S()

    # Assert
    assert "use sigmacro_process_figure_s() instead" in str(caught[0].message)


def test_deprecated_alias_still_prints_output_when_warnings_silenced():
    # Arrange
    buf = StringIO()

    # Act
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with _swap_stdout(buf):
            SigMacro_processFigure_S()

    # Assert
    assert buf.getvalue().strip() != ""


# ---------------------------------------------------------------------------
# Docstring + side-effect properties
# ---------------------------------------------------------------------------


def test_sigmacro_process_figure_s_has_docstring_attached():
    # Arrange
    fn = sigmacro_process_figure_s

    # Act
    doc = fn.__doc__

    # Assert
    assert doc is not None


def test_sigmacro_process_figure_s_docstring_mentions_sigmaplot():
    # Arrange
    doc = sigmacro_process_figure_s.__doc__ or ""

    # Act
    mentions_sigmaplot = "SigmaPlot" in doc

    # Assert
    assert mentions_sigmaplot


def test_sigmacro_process_figure_s_docstring_mentions_macro():
    # Arrange
    doc = (sigmacro_process_figure_s.__doc__ or "").lower()

    # Act
    mentions_macro = "macro" in doc

    # Assert
    assert mentions_macro


def test_sigmacro_process_figure_s_restores_stdout_after_call():
    # Arrange
    original_stdout = sys.stdout
    buf = StringIO()

    # Act
    with _swap_stdout(buf):
        sigmacro_process_figure_s()

    # Assert
    assert sys.stdout is original_stdout


def test_sigmacro_process_figure_s_produces_deterministic_output_across_calls():
    # Arrange
    outputs = []

    # Act
    for _ in range(3):
        buf = StringIO()
        with _swap_stdout(buf):
            sigmacro_process_figure_s()
        outputs.append(buf.getvalue())

    # Assert
    assert outputs[0] == outputs[1] == outputs[2]


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])

# EOF
