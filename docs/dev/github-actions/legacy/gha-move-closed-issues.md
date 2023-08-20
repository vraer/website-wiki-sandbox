## Summary
Moves a closed issue into either the QA or Done column of the project board. If the issue has a “hard” label (Feature: Refactor CSS, Feature: Refactor HTML, Feature: Refactor JS / Liquid, Feature: Refactor GH), the issue is moved to the Done column. If the issue has no “hard” labels but does have an “override” label (role: front end), the issue is moved to the QA column. If the issue has no “hard” or “override” labels and does have a “soft” label (role: back end/devOps, Feature: Analytics), it is moved to Done. All other issues are moved to QA.
### Scheduled
- Issue closed
### Workflow
- [move-closed-issues.yaml](https://github.com/hackforla/website/blob/gh-pages/.github/workflows/move-closed-issues.yaml)
### Supporting Files/Folders
- Supporting Files Folder: [move-closed-issues](https://github.com/hackforla/website/tree/gh-pages/github-actions/move-closed-issues)
---
Back to [HfLA GitHub Actions](HfLA-GitHub-Actions)