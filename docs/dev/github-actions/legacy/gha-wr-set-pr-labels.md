## Summary
This workflow is triggered when workflow [Set PR labels] is completed. Downloads artifact for the completed workflow. Then, gets the PR and issue number from the downloaded artifact and uses an API request to get the labels. Lastly, puts the same labels into the PR.

### Scheduled
- Workflow [Set PR Labels] completed

### Workflow
- [wr-set-pr-labels.yaml](https://github.com/hackforla/website/blob/gh-pages/.github/workflows/wr-set-pr-labels.yaml)

### Supporting Files/Folders
- https://github.com/hackforla/website/tree/gh-pages/github-actions/trigger-pr

---
Back to [HfLA GitHub Actions](HfLA-GitHub-Actions)