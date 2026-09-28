---
name: review-issue
description: Review the current diff against a GitHub issue and repository rules without changing files. Use after implementation and before publication.
argument-hint: "[issue-number]"
arguments:
  - issue
disable-model-invocation: true
disallowed-tools:
  - Edit
  - Write
---

# Review GitHub issue $issue

If the issue number is missing, ask for it and stop.

1. Read the GitHub issue `$issue` with `gh issue view $issue`. Then read
   `CONTRIBUTING.md`, `CLAUDE.md`, and the current Git diff.
2. Check acceptance-criteria coverage, logic, invariants, regression-test
   quality, preserved behavior, public API stability, and scope creep.
3. Report only actionable findings. For each finding, give:
   - severity: `BLOCKING`, `WARNING`, or `SUGGESTION`;
   - file and line;
   - the problem and its risk; and
   - the smallest correction.
4. If there are no actionable findings, say so and list the evidence checked.

Do not edit files, commit, push, create a pull request, or merge.
