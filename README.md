# scitex-gists

SigmaPlot macro conversion utilities for matplotlib.

## Problem and Solution


| # | Problem | Solution |
|---|---------|----------|
| 1 | **SigmaPlot v12 macro files live outside version control** -- one lab machine has them, nobody else does | **Python prints the macro** -- `sigmacro_process_figure_s()` emits VB-style macro text; copy-paste into SigmaPlot editor; macros are now part of the repo |

## Installation

```bash
pip install scitex-gists
```

## Usage

```python
from scitex_gists import sigmacro_process_figure_s, sigmacro_to_blue

# Convert SigmaPlot figure-processing macro
sigmacro_process_figure_s()

# Convert SigmaPlot color macro
sigmacro_to_blue()
```

## License

AGPL-3.0
