# Tiny Checkout project instructions

## Project

- `checkout.py` owns the calculation.
- `tests/test_checkout.py` owns its unit tests.
- Monetary amounts are integer cents.
- Follow `CONTRIBUTING.md` for the Git workflow.

## Commands

Run the complete suite from this directory:

```bash
python3 -m unittest discover -s tests -v
```

Run one test by giving its dotted test name to `python3 -m unittest -v`.

## Working rules

1. For a bug, inspect the GitHub issue, implementation, and existing tests
   before proposing a change.
2. In Plan mode, do not edit source or test files. Report the reproducer,
   cause with supporting code or test evidence, acceptance-criteria mapping,
   smallest proposed change, and open questions.
3. Wait for explicit approval before implementation.
4. Add a regression test and run it before the fix. Confirm that it fails for
   the reported reason.
5. Make the smallest change that satisfies the approved acceptance criteria.
   Do not add dependencies, redesign the discount system, or perform unrelated
   cleanup.
6. Run the targeted test and complete suite after the fix. Report commands
   actually run and their outcomes.
7. Do not start a code review yourself. After implementation, wait for the
   user to invoke `/review-issue` with the GitHub issue number.
8. Do not commit, push, or create a pull request until the user explicitly
   approves that action.
9. Never merge a workshop pull request.

## Skills

`/review-issue` is the project review workflow. It is human-triggered and
read-only. It takes a GitHub issue number, compares the current diff with that
issue and the repository rules, and reports findings. Do not invoke it unless
the user does.
