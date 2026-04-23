<!-- 01_quick-start.md -->

# scitex-gists — Quick Start

## Install

```bash
pip install scitex-gists
```

## Import

```python
import scitex_gists
```

## Print the panel-formatting macro

```python
from scitex_gists import sigmacro_process_figure_s

sigmacro_process_figure_s()
# Prints a SigmaPlot v12 VB macro to stdout. Copy it into
# SigmaPlot's macro editor (Tools > Macro > Edit).
```

## Print the "change selection to blue" macro

```python
from scitex_gists import sigmacro_to_blue

sigmacro_to_blue()
```

The PascalCase names (`SigMacro_processFigure_S`, `SigMacro_toBlue`) are
retained as aliases for backward compatibility. New code should use the
snake_case forms above.

See SigmaPlot's "Automating Routine Tasks" section for how to load the
printed macros.
