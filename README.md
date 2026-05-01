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

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>SigmaPlot macro printers — version-controlled VB-style macros emitted from Python.</b></p>

<p align="center">
  <a href="https://scitex-gists.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-gists</code>
</p>

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **SigmaPlot v12 macro files live outside version control** — one lab machine has them, nobody else does | **Python prints the macro** — `sigmacro_process_figure_s()` emits VB-style macro text; copy-paste into SigmaPlot editor; macros are now part of the repo |

## Installation

```bash
pip install scitex-gists
```

## Quick Start

```python
from scitex_gists import sigmacro_process_figure_s, sigmacro_to_blue

sigmacro_process_figure_s()   # prints the figure-processing macro
sigmacro_to_blue()            # prints the color macro
```

## 1 Interfaces

<details>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_gists import sigmacro_process_figure_s, sigmacro_to_blue

sigmacro_process_figure_s()
sigmacro_to_blue()
```

Each function prints VB-style macro text to stdout. Pipe into your
clipboard or redirect to a file, then paste into the SigmaPlot macro
editor.

</details>

## Part of SciTeX

`scitex-gists` is part of [**SciTeX**](https://scitex.ai).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
