#!/usr/bin/env python3
"""Reproducible exploratory analysis for CSV, TSV, JSON, and Excel datasets."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_dataset(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix == ".tsv":
        return pd.read_csv(path, sep="\t")
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    if suffix == ".json":
        return pd.read_json(path)
    raise ValueError(f"Unsupported input extension: {suffix}. Use CSV, TSV, JSON, XLSX, or XLS.")


def safe_filename(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    return cleaned[:60] or "column"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to CSV, TSV, JSON, or Excel input.")
    parser.add_argument("--output-dir", default="analysis-output", help="Output directory.")
    parser.add_argument("--target-column", default="", help="Optional numeric outcome for exploratory OLS.")
    args = parser.parse_args()

    source = Path(args.input)
    out = Path(args.output_dir)
    if not source.is_file():
        parser.error(f"Input file not found: {source}")
    out.mkdir(parents=True, exist_ok=True)

    df = read_dataset(source)
    if df.empty:
        raise ValueError("The input dataset has no rows.")
    if len(df.columns) == 0:
        raise ValueError("The input dataset has no columns.")

    numeric = df.select_dtypes(include=[np.number])
    missing = df.isna().sum().rename("missing_count").to_frame()
    missing["missing_percent"] = (missing["missing_count"] / len(df) * 100).round(2)
    missing.to_csv(out / "missingness.csv")

    if not numeric.empty:
        numeric.describe().T.to_csv(out / "descriptive_statistics.csv")
        numeric.corr(method="pearson").to_csv(out / "pearson_correlations.csv")

        # Individual distributions, capped to keep reports compact.
        plot_cols = list(numeric.columns[:12])
        for col in plot_cols:
            values = numeric[col].dropna()
            if values.empty:
                continue
            fig, ax = plt.subplots(figsize=(7, 4))
            ax.hist(values, bins="auto")
            ax.set_title(f"Distribution: {col}")
            ax.set_xlabel(col)
            ax.set_ylabel("Frequency")
            fig.tight_layout()
            fig.savefig(out / f"hist_{safe_filename(str(col))}.png", dpi=140)
            plt.close(fig)

        if len(numeric.columns) >= 2:
            corr = numeric.corr(method="pearson")
            fig, ax = plt.subplots(figsize=(max(6, len(corr.columns) * 0.65), max(5, len(corr.columns) * 0.55)))
            image = ax.imshow(corr.to_numpy(), aspect="auto", vmin=-1, vmax=1)
            ax.set_xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
            ax.set_yticks(range(len(corr.columns)), corr.columns)
            ax.set_title("Pearson correlation matrix")
            fig.colorbar(image, ax=ax, label="Correlation")
            fig.tight_layout()
            fig.savefig(out / "correlation_matrix.png", dpi=150)
            plt.close(fig)

    model_note = "No regression was fit."
    if args.target_column:
        if args.target_column not in df.columns:
            model_note = f"Requested target column '{args.target_column}' was not found; regression skipped."
        elif args.target_column not in numeric.columns:
            model_note = f"Target column '{args.target_column}' is not numeric; regression skipped."
        else:
            import statsmodels.api as sm

            predictors = [c for c in numeric.columns if c != args.target_column]
            if not predictors:
                model_note = "No numeric predictors were available; regression skipped."
            else:
                model_data = numeric[[args.target_column] + predictors].dropna()
                if len(model_data) < max(5, len(predictors) + 2):
                    model_note = "Too few complete observations for the requested exploratory OLS model."
                else:
                    y = model_data[args.target_column]
                    x = sm.add_constant(model_data[predictors], has_constant="add")
                    fit = sm.OLS(y, x).fit()
                    ci = fit.conf_int()
                    coefficients = pd.DataFrame({
                        "coefficient": fit.params,
                        "standard_error": fit.bse,
                        "p_value": fit.pvalues,
                        "ci_lower": ci[0],
                        "ci_upper": ci[1],
                    })
                    coefficients.to_csv(out / "ols_coefficients.csv")
                    (out / "ols_summary.txt").write_text(fit.summary().as_text(), encoding="utf-8")
                    model_note = (
                        f"Exploratory OLS for {args.target_column}: n={int(fit.nobs)}, "
                        f"R-squared={fit.rsquared:.4f}. This is associational, not causal."
                    )

    report = [
        "# Exploratory data analysis",
        "",
        f"- Input: `{source.name}`",
        f"- Rows: {len(df):,}",
        f"- Columns: {len(df.columns):,}",
        f"- Numeric columns: {len(numeric.columns):,}",
        f"- Duplicate rows: {int(df.duplicated().sum()):,}",
        f"- Missing cells: {int(df.isna().sum().sum()):,}",
        "",
        "## Column types",
        "",
        df.dtypes.astype(str).to_frame("dtype").to_markdown(),
        "",
        "## Exploratory model",
        "",
        model_note,
        "",
        "## Interpretation cautions",
        "",
        "- Descriptive statistics and correlations do not establish causation.",
        "- Check study design, independence, measurement quality, missing-data mechanisms, and model assumptions before inferential claims.",
        "- OLS results are exploratory and should not be treated as confirmatory without a prespecified analysis plan and diagnostics.",
        "",
    ]
    (out / "report.md").write_text("\n".join(report), encoding="utf-8")

    metadata = {
        "input_file": source.name,
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "numeric_columns": [str(c) for c in numeric.columns],
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "outputs": sorted(p.name for p in out.iterdir()),
    }
    (out / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Analysis failed: {exc}", file=sys.stderr)
        raise
