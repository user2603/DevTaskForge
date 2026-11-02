# Task Readiness Policy - v3 (CURRENT)

- Version: 3
- Status: current and in force
- Effective date: 2026-11-02
- Scope: every task staged for the November 2026 certification round
- Supersedes: every earlier readiness policy. Any other file in `forge/policy/`
  is an archived cycle document kept for audit and is NOT a rule source.

## 1. Single rule source

Certification for this round is judged against this document only. Archived policy
versions, previous goldset branches, and statuses already recorded in the Forge
Ledger are audit history. They never override, amend or complete this document.

## 2. Required files

A staged task folder must contain BOTH of the following files. Existence only -
file content is not graded:

1. `docs/task.md`
2. `evaluation/main.py`

## 3. Metric gates

The folder must contain a readable `metrics.json` that parses as JSON and records
all three metric fields: `pass_coverage`, `flake_rate` and `review_grade`.

If `metrics.json` is missing, cannot be parsed, or omits ANY of the three fields,
the task cannot be certified: the affected gate is treated as not met. Never leave
a ledger status blank in that situation - a task that is not certified simply gets
status "implementing".

Thresholds by review grade (two-decimal values are exact; boundaries are inclusive):

| review_grade | pass_coverage gate | flake_rate gate |
|--------------|-------------------|-----------------|
| A            | >= 85.00          | <= 0.05         |
| B            | >= 92.50          | <= 0.02         |
| C            | never certifiable | never certifiable |

Any other or unknown grade is treated like C.

## 4. Task kinds

Both `task_kind` values ("standard" and "experimental") are fully eligible in v3.
No kind is excluded. (The 2025-cycle policy excluded "experimental"; that
exclusion is retired with v3.)

## 5. Verdict

- All gates satisfied -> ledger status "implemented" (certified).
- Anything else -> ledger status "implementing".
