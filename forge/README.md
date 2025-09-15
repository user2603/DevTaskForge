# DevTaskForge

Shared staging repo for automation-task candidates.

Layout:

- `forge/policy/` - readiness policies. The current one is
  `readiness_policy_v3_current.md`; every other policy file is an archived cycle
  document kept for audit.
- `forge/examples/example-task/` - canonical folder layout (format reference
  only, not part of any round).
- `forge/tasks/<contributor>/<task-name>/` - one folder per task, living on the
  contributor's `dev/<contributor>` branch.
- `forge/goldset/` - destination used by certification rounds when the goldset
  branch is cut.

How a round works:

1. Contributors stage new task folders on their `dev/<contributor>` branch.
2. The current readiness policy decides whether a staged task is certified
   ("implemented") or still in progress ("implementing").
3. Certified tasks are recorded in the Forge Ledger (Notion) and copied under
   `forge/goldset/` on the `goldset` branch.

Note: commit messages are informal. A round is defined by the current policy and
by what the latest task-adding commit on each branch actually contains, not by
what a message claims.
