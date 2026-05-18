---
description: |
  [TOPIC] scitex-gists Quick Start
  [DETAILS] Smallest example — print SigmaPlot v12 macros to stdout, then paste into SigmaPlot's macro editor.
tags: [scitex-gists-quick-start]
---

# Quick Start

## Print the panel-formatting macro

```python
from scitex_gists import sigmacro_process_figure_s

sigmacro_process_figure_s()
# Prints a SigmaPlot v12 VB macro to stdout. Copy it into
# SigmaPlot's macro editor (Tools > Macro > Edit).
```

## Print the "recolor selection to blue" macro

```python
from scitex_gists import sigmacro_to_blue

sigmacro_to_blue()
```

## Capture instead of printing

Both functions write to stdout, not return strings. To capture:

```python
import io, contextlib
from scitex_gists import sigmacro_to_blue

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    sigmacro_to_blue()
macro_text = buf.getvalue()
```

## Backward-compatible aliases

The PascalCase names (`SigMacro_processFigure_S`, `SigMacro_toBlue`)
are retained as aliases. New code should use the snake_case forms above.

See SigmaPlot's "Automating Routine Tasks" docs for how to load the
printed macros into the macro editor.
