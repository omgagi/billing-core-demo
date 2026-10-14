# Governance evidence

This repo demonstrates that a change can only reach `main` if **CI passes** and a
**human other than the author approves** it.

## Controls on `main` (branch protection)
- Pull request required; direct pushes, force pushes and deletions blocked.
- 1 approving review required; stale approvals dismissed on new commits;
  the most recent push must be approved by someone other than its pusher.
- Code-owner review required (`.github/CODEOWNERS` → `@adminomegacortex`).
- Required status check `test` (`.github/workflows/ci.yml`), branch must be up to date.
- Rules enforced for admins too.

Author identity: `@omgagi` (automation). Approver: `@adminomegacortex` (Ivan). GitHub
does not allow an author to approve their own pull request.

## Evidence PRs
| PR | What it shows | Outcome |
|----|---------------|---------|
| [#3 evidence: failing test blocks merge](https://github.com/omgagi/billing-core-demo/pull/3) | Deliberate bug (tax always rounds up). CI `test` fails. | Merge blocked by required check; closed as rejected. |
| [#4 evidence: unauthorized access attempt](https://github.com/omgagi/billing-core-demo/pull/4) | Tries to empty CODEOWNERS, widen workflow permissions and skip tests. | Merge blocked: needs approval from a reviewer other than the author; closed as rejected. |
| [#2 fix: corrected change](https://github.com/omgagi/billing-core-demo/pull/2) | Real fix (round tax halves-up) + test + CI + CODEOWNERS + this file. CI green. | Waits for `@adminomegacortex` approval before it can merge. |

#3 and #4 are built on top of #2's branch so the CI workflow exists and runs in them.

## Reproduce
    python3 -m unittest discover -s tests -t . -v
- On `main` (before #2): `test_tax_of_half_a_cent_or_more_rounds_up` fails.
- On #2: all tests pass. On #3: rounding tests fail.
- Try merging #3 or #4 (or #2 without approval): GitHub refuses.
