---
name: scitex-gists
description: |
  [WHAT] SigmaPlot v12 macro snippets as printable Python functions — for researchers who still format figures in SigmaPlot and want reproducible VB-style macros stashed in a Python environment.
  [WHEN] Use whenever the user asks to "get the SigmaPlot figure-formatting macro", "print the VB macro for blue recolor", "auto-format a SigmaPlot figure", or mentions `scitex.
  [HOW] `pip install scitex-gists` then `import scitex_gists`; see leaf skills for details.
tags: [scitex-gists]
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  http: 0
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

- [01_installation.md](01_installation.md) — pip install + smoke verify
- [02_quick-start.md](02_quick-start.md) — print macros + capture pattern
- [03_python-api.md](03_python-api.md) — public callables reference
- [10_quick-start.md](10_quick-start.md) — original quick-start (legacy)
- [11_python-api.md](11_python-api.md) — original API page (legacy)

No CLI, no MCP tools, no extra modules.
