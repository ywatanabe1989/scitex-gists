---
description: |
  [TOPIC] scitex-gists Installation
  [DETAILS] pip install scitex-gists; pure-Python (no extras); smoke verify.
tags: [scitex-gists-installation]
---

# Installation

## Standard

```bash
pip install scitex-gists
```

Pure-Python with no runtime dependencies. The package only contains
SigmaPlot v12 VB macro snippets returned/printed as Python strings.

## Umbrella

```bash
pip install scitex            # also exposes the same module as scitex.gists
```

`pip install scitex-gists` alone does NOT make `import scitex.gists`
work — install the umbrella for that form. See
`../../general/02_interface-python-api.md`.

## Verify

```bash
python -c "import scitex_gists; print(scitex_gists.__version__); scitex_gists.sigmacro_to_blue()"
```

Expected: a version string, then the SigmaPlot VB macro text printed
to stdout.

## When NOT to install

- You don't use SigmaPlot v12 — this package is purpose-built for that
  one workflow. There is no general-purpose API here.
- You want figure-formatting in Python — use `scitex-plt` (figrecipe)
  instead.
