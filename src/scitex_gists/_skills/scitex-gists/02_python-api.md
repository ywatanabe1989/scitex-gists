---
name: python-api
description: scitex-gists — Python API — see file body for details.
tags: [scitex-gists, scitex-package]
---

<!-- 02_python-api.md -->

# scitex-gists — Python API

All public symbols are in `scitex_gists.__all__`:

| Symbol | Kind | One-liner |
|--------|------|-----------|
| `sigmacro_process_figure_s` | function | Print SigmaPlot v12 macro that formats a panel. |
| `sigmacro_to_blue` | function | Print SigmaPlot v12 macro that recolors the selection to blue. |
| `SigMacro_processFigure_S` | function | PascalCase alias of `sigmacro_process_figure_s`. |
| `SigMacro_toBlue` | function | PascalCase alias of `sigmacro_to_blue`. |

## Signatures

```python
sigmacro_process_figure_s() -> None
sigmacro_to_blue() -> None
```

Both take no arguments and write the macro text to stdout. They do not
return the macro as a string — redirect stdout if you need to capture it.
