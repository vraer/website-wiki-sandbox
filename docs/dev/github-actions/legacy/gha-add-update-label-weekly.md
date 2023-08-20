## Summary
Checks the in-progress column from the project board. Goes through each issue, and if there is an assignee, checks the timeline for the issue. If it is outdated, posts a comment to update the issue and ensures the label is changed to 'To Update !'. Otherwise, add the 'Status: Updated' label.

### Scheduled
- Scheduled to run at 7:00 AM every Friday

### Workflow: 
- [add-update-label-weekly.yml](https://github.com/hackforla/website/blob/gh-pages/.github/workflows/add-update-label-weekly.yml)
- [add-label.js](https://github.com/hackforla/website/blob/gh-pages/github-actions/add-update-label-weekly/add-label.js)

Every Friday at 7:00 AM, run add-label.js on the project board in-progress column, which works as follows:
1. Checks the timeline for all issues in the project board column.
2. Based on an issue's timeline (I.e. Date of issue creation plus recent comments or cross-references), add or remove labels and post a comment on issue timeline accordingly.

### Supporting Files/Folder: 
- [add-update-label-weekly](https://github.com/hackforla/website/tree/gh-pages/github-actions/add-update-label-weekly)
    * File: https://github.com/hackforla/website/blob/gh-pages/github-actions/add-update-label-weekly/add-label.js references
      * https://github.com/hackforla/website/blob/gh-pages/github-actions/add-update-label-weekly/update-instructions-template.md (same folder)
      * https://github.com/hackforla/website/blob/gh-pages/github-actions/utils/find-linked-issue.js (utils folder)




