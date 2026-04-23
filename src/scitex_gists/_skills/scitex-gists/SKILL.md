---
name: scitex-gists
description: Grab-bag of SigmaPlot (v12) automation macros — two functions that print VB-style macros for figure formatting. Copy the printed output into SigmaPlot's macro editor.
user-invocable: false
---

# scitex-gists

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
