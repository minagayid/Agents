---
name: exploratory-data-analysis
description: Run a structured exploratory data analysis (EDA) on a dataset to surface distributions, relationships, and issues. Use when the user asks to explore, understand, or summarize a dataset.
---

# Exploratory Data Analysis

Understand a dataset before modeling or drawing conclusions.

## Steps
1. **Frame the question.** What decision or hypothesis is this analysis serving?
2. **Overview.** Shape, dtypes, missingness, memory; identify id/target/feature roles.
3. **Univariate.** Distribution of each variable — histograms/boxplots for numeric, value counts for
   categorical. Note skew, spread, outliers, rare categories.
4. **Bivariate / multivariate.** Relationships to the target and among features: correlations,
   grouped stats, scatter/box by category. Watch for confounders.
5. **Quality issues.** Missing patterns (random vs. systematic), inconsistent categories, leakage,
   class imbalance, duplicated or near-constant columns.
6. **Summarize findings** with the visuals that carry the insight (see the `dataviz` guidance for
   good chart/color choices) and a short list of implications.

## Guidelines
- Let the data surprise you — don't just confirm the expected story.
- Prefer clear visuals over tables of raw numbers; label axes and units.
- Distinguish correlation from causation explicitly.
- Record concrete next steps: features to engineer, data to fix, questions raised.
- Keep it reproducible (a notebook/script), seeded where randomness is involved.
