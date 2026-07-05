---
name: data-cleaning
description: Clean and prepare a tabular dataset (missing values, types, duplicates, outliers) for analysis. Use when the user asks to clean data, wrangle a CSV/dataframe, or prep data for modeling.
---

# Data Cleaning

Turn messy tabular data into a trustworthy, analysis-ready dataset — without silently distorting it.

## Steps
1. **Profile** before changing anything: shape, dtypes, `head()`, per-column null counts,
   uniques, value ranges, and summary stats. Understand what each column *means*.
2. **Fix types.** Parse dates, cast numerics, normalize categoricals; strip stray whitespace/units.
3. **Missing values.** Decide per column, with intent: drop rows/cols, impute (mean/median/mode/model),
   or flag with an indicator. Never impute the target for supervised ML.
4. **Duplicates.** Detect exact and key-based duplicates; dedupe deliberately, keep a record of how many.
5. **Outliers & errors.** Range/consistency checks (negative ages, future dates, impossible values);
   investigate before removing — an outlier may be the signal.
6. **Standardize.** Consistent units, categories, casing, and encodings; tidy column names.
7. **Validate.** Row counts before/after, invariants hold, spot-check samples.

## Guidelines
- Keep the raw data immutable; do cleaning in a reproducible script/notebook, not by hand.
- Log every transformation and how many rows it affected — cleaning must be auditable.
- Document assumptions (why you imputed, what you dropped) alongside the output.
- Beware leakage: don't use future/target information when preparing features.
