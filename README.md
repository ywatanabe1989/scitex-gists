# scitex-gists

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-gists.svg)](https://pypi.org/project/scitex-gists/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-gists.svg)](https://pypi.org/project/scitex-gists/)
[![Tests](https://github.com/ywatanabe1989/scitex-gists/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-gists/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-gists/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-gists/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-gists/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-gists)
[![Docs](https://readthedocs.org/projects/scitex-gists/badge/?version=latest)](https://scitex-gists.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


SigmaPlot macro conversion utilities for matplotlib.

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

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
