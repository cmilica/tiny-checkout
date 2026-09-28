# Contributing

Keep changes small enough to review from the Git diff.

## Workflow

1. Start from a clean `main` branch.
2. Create your own branch from `main`:
   `workshop/<your-github-handle>-issue-1`.
3. Reproduce the issue before editing.
4. Add a regression test that fails for the reported behavior.
5. Make the smallest change that satisfies the issue.
6. Run the targeted test and the complete suite.
7. Inspect the diff before committing.
8. Review against the GitHub issue with `/review-issue` before publication.
9. Open a draft pull request linking that GitHub issue. Do not merge workshop
   pull requests.

## Test command

```bash
python3 -m unittest discover -s tests -v
```

## Commit and pull request

- Use a short imperative commit subject.
- Link the GitHub issue in the pull-request description.
- Record the exact verification command and result.
- Explain any scope or review decision that is not obvious from the diff.
- Do not include generated files, environment files, or unrelated cleanup.
