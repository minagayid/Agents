---
name: sql-optimizer
description: Diagnose and speed up slow SQL queries (indexes, query shape, execution plans). Use when the user shares a slow query, asks to optimize SQL, or asks why a query is slow.
---

# SQL Optimizer

Make slow queries fast without changing their results.

## Process
1. **Measure first.** Get the execution plan: `EXPLAIN ANALYZE` (Postgres/MySQL 8+),
   `EXPLAIN QUERY PLAN` (SQLite). Identify the costliest node and row estimates vs. actuals.
2. **Find the bottleneck.** Common culprits:
   - Sequential/full scans on large tables where an index would help.
   - Missing index on `JOIN`/`WHERE`/`ORDER BY` columns.
   - `SELECT *` pulling unneeded columns; functions on indexed columns preventing index use.
   - N+1 query patterns from the app layer.
   - Bad cardinality estimates → stale statistics (`ANALYZE`).
3. **Fix the highest-impact issue**, then re-measure. Change one thing at a time.

## Techniques
- Add a targeted (often composite) index matching the filter+sort; put equality columns before range.
- Rewrite to be **sargable**: `WHERE created_at >= $1` instead of `WHERE date(created_at) = $1`.
- Select only needed columns; consider a covering index.
- Replace correlated subqueries with joins or `EXISTS` where clearer/faster.
- Paginate with keyset (`WHERE id > $last`) instead of large `OFFSET`.
- For aggregates over big tables, consider materialized views / summary tables.

## Guidelines
- Verify the optimized query returns identical results.
- Note the trade-off: indexes speed reads but cost writes and storage.
- Report before/after timings and the plan change, not just the new query.
