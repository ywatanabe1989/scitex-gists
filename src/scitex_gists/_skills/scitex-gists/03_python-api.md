---
description: |
  [TOPIC] scitex-gists Python API
  [DETAILS] Top-level public callables — sigmacro_process_figure_s, sigmacro_to_blue, plus PascalCase aliases.
tags: [scitex-gists-python-api]
---

# Python API

All public symbols are in `scitex_gists.__all__`.

## Public symbols

| Name                          | Kind     | Purpose                                                |
|-------------------------------|----------|--------------------------------------------------------|
| `__version__`                 | str      | Installed package version                              |
| `sigmacro_process_figure_s()` | function | Print SigmaPlot v12 macro that formats a panel         |
| `sigmacro_to_blue()`          | function | Print SigmaPlot v12 macro that recolors selection blue |
| `SigMacro_processFigure_S`    | alias    | PascalCase alias of `sigmacro_process_figure_s`        |
| `SigMacro_toBlue`             | alias    | PascalCase alias of `sigmacro_to_blue`                 |

## Signatures

```python
sigmacro_process_figure_s() -> None
sigmacro_to_blue() -> None
```

Both take no arguments and write the macro text to **stdout**. They do
not return the macro as a string — see `02_quick-start.md` for the
`contextlib.redirect_stdout` capture pattern.

## Design notes

- The package intentionally has no public `Macro` class or registry.
  Each macro is a single function that prints fixed text — agents can
  read the source as the source of truth.
- New macros are added by writing a `_SigMacro_*.py` module under
  `scitex_gists/` and re-exporting both naming forms.

## Not exposed

- No SigmaPlot automation/IPC layer — these are text macros only.
- No alternative output formats (HTML, JSON, etc.).
