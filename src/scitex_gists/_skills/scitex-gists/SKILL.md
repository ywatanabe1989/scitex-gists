---
name: scitex-gists
description: SigmaPlot v12 macro snippets as printable Python functions — for researchers who still format figures in SigmaPlot and want reproducible VB-style macros stashed in a Python environment. Public API (4 symbols, 2 pairs of snake_case + legacy camelCase aliases) — `sigmacro_process_figure_s()` / `SigMacro_processFigure_S()` (print a VB macro that applies SigmaPlot figure-processing defaults — axis/line widths, fonts, tick sizes), `sigmacro_to_blue()` / `SigMacro_toBlue()` (print a macro that recolors a SigmaPlot figure's series to a blue palette). Both functions emit macro text to stdout — copy-paste into SigmaPlot's macro editor. No CLI, no MCP tools, intentionally narrow. Drop-in replacement for maintaining VB `.sbm` macro files outside version control, stashing SigmaPlot formatting instructions in lab notebooks, or re-deriving figure style every time. Use whenever the user asks to "get the SigmaPlot figure-formatting macro", "print the VB macro for blue recolor", "auto-format a SigmaPlot figure", or mentions `scitex.gists`, SigMacro, SigmaPlot v12 automation.
user-invocable: false
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  hook: 0
  http: 0
tags: [scitex-gists, scitex-package]
---

# scitex-gists

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

Tiny utility package hosting SigmaPlot macro snippets as Python functions
that `print` the macro text. Intended for researchers who still use
SigmaPlot v12 and want a reproducible way to stash figure-formatting
macros in a Python environment. Do not expect a broad API.

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-gists
import scitex_gists
scitex_gists.sigmacro_process_figure_s(...)

# Umbrella — pip install scitex
import scitex.gists
scitex.gists.sigmacro_process_figure_s(...)
```

`pip install scitex-gists` alone does NOT expose the `scitex` namespace;
`import scitex.gists` raises `ModuleNotFoundError`. To use the
`scitex.gists` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

## Sub-skills

- [01_quick-start.md](01_quick-start.md) — install, import, usage snippets
- [02_python-api.md](02_python-api.md) — public symbols and signatures

No CLI, no MCP tools, no extra modules.
