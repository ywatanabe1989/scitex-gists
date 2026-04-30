#!/usr/bin/env python3
"""Quickstart for scitex-gists: print SigmaPlot macros."""

import scitex_gists


def main() -> int:
    print(f"scitex_gists exports: {scitex_gists.__all__}")

    print("\n--- sigmacro_to_blue ---")
    scitex_gists.sigmacro_to_blue()

    print("\n--- sigmacro_process_figure_s ---")
    scitex_gists.sigmacro_process_figure_s()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
