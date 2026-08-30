# Task Readiness Policy - v2 (2025 CYCLE - ARCHIVED)

- Status: ARCHIVED - retained for audit only. NOT valid for any certification
  round after 2026-11-01. The current policy supersedes this file.
- Cycle: 2025 H2

## Required files

- `docs/task.md` (existence only)

## Metric gates

One scale for every review grade:

- pass_coverage >= 80.00
- flake_rate <= 0.10

## Task kinds

- "experimental" tasks are excluded from certification.

## Missing data

- If `metrics.json` parses but omits an individual field, the task is
  grandfathered: the missing gate does not block certification.
- This grandfathering applies to omitted fields only. A task whose
  `metrics.json` is missing entirely or cannot be parsed has no recorded
  metrics and cannot be certified.

## Verdict

- Gates satisfied -> "implemented".
- Otherwise -> "implementing".
