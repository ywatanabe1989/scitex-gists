#!/usr/bin/env python3
"""SigmaPlot macro conversion utilities."""

from __future__ import annotations

try:
    from importlib.metadata import version as _v, PackageNotFoundError
    try:
        __version__ = _v("scitex-gists")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"

from ._SigMacro_processFigure_S import (
    SigMacro_processFigure_S,
    sigmacro_process_figure_s,
)
from ._SigMacro_toBlue import SigMacro_toBlue, sigmacro_to_blue

__all__ = [
    "__version__",
    "SigMacro_processFigure_S",
    "SigMacro_toBlue",
    "sigmacro_process_figure_s",
    "sigmacro_to_blue",
]
