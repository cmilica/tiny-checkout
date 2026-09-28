# Tiny Checkout

`tiny-checkout` calculates an order discount and final total. Amounts are
integer cents, so the example does not depend on floating-point currency
rounding.

This is the Tiny Checkout repository for the Week 4 guided lab. Clone it from
the URL on the course page. Run Claude from this repository root. Claude
edits `checkout.py` and `tests/test_checkout.py` here, and the draft pull
request is opened here.

Keep the course's `guided_lab/README.md` open in another window. It contains
the step-by-step exercise. Your task is **GitHub issue #1** in this
repository.

## Requirements

- Python 3.9 or newer
- Git
- Claude Code
- GitHub CLI (`gh`) for the draft-PR step

No Python packages are required.

## Run the tests

From this directory:

```bash
python3 -m unittest discover -s tests -v
```

The prepared baseline has six passing tests. A green baseline does not prove
that every required behavior has a test.

## Repository map

- `checkout.py`: application code. Claude will make the bug fix here.
- `tests/test_checkout.py`: test code. Claude will add the regression test
  here.
- `CONTRIBUTING.md`: branch, test, and pull-request conventions for people and
  Claude.
- `CLAUDE.md`: persistent project instructions loaded into sessions started
  from this repository root.
- `.claude/settings.json`: permission rules enforced by Claude Code.
- `.claude/skills/review-issue/SKILL.md`: an on-demand, read-only review
  workflow invoked as `/review-issue <issue-number>`.
- `.github/workflows/tests.yml`: the CI test run.
- `.github/pull_request_template.md`: the evidence expected in the draft PR.

## How the agent setup works

You do not write an agent program in this repository. Claude Code provides the
agent runtime; the repository supplies code, instructions, a skill, and
permission settings.

### Agent

Claude Code is the agent runtime. Start it from this repository root with:

```bash
claude
```

### Rules

`CLAUDE.md` tells Claude to:

- investigate before editing;
- wait for plan approval;
- add and run a regression test before the fix;
- keep the change small;
- run the targeted and complete tests; and
- wait for approval before commit, push, or PR creation.

These are instructions in Claude's context. They guide behavior but do not
enforce tool access.

### Permissions

`.claude/settings.json` controls tool access:

- the complete test command, issue query, status, and diff are allowed;
- file writes and Git publication ask for approval; and
- listed destructive commands and direct `.env` reads are blocked.

Permission rules control actions. They do not prove that the implementation is
correct.

### Skills

The project includes one skill: `/review-issue`.

Run `/review-issue 1` after implementation to compare the current diff with
GitHub issue #1 and the repository rules. The skill is intentionally:

- **on demand:** `disable-model-invocation: true` means only you can start it;
- **reusable:** the issue number is an argument rather than hard-coded; and
- **read only for its invocation:** `disallowed-tools` removes `Edit` and
  `Write` while it runs.

Unlike `CLAUDE.md`, the full skill body is not loaded into every session. It
enters context when you invoke it. Unlike ordinary prose instructions, its
tool restriction is enforced by the runtime for that invocation. The
repository's permission settings still apply to all remaining tools.

### Workflow

Follow the Week 4 guided-lab page. It tells you when to investigate, approve,
implement, invoke the review skill, verify, and publish. `CLAUDE.md` keeps only
the project rules that should be available in every new session.

Do not change the code before the guided session begins.
