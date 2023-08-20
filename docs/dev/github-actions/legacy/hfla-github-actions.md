#### Workflows are yaml files
#### Supporting files can be
* js
* json
* md
* gitkeep

### Template for GHA documentation
```
## Summary
### Scheduled
-
### Workflow
-
### Supporting Files/Folders
-
---
Back to [HfLA GitHub Actions](HfLA-GitHub-Actions)
```

### Hack for LA's GHAs
#### [add update label weekly](GHA:-add-update-label-weekly)
- Checks the in-progress column from the project board. Goes through each issue, and if there is an assignee, checks the timeline for the issue. If it is outdated, posts a comment to update the issue and ensures the label is changed to 'to update.' Else, change the label so it is 'updated'

#### [github data](GHA:-github-data)
- Generates a new github-data.json and commits that to the repository

#### [issue trigger](GHA:-issue-trigger)
- Check if an issue has the three required labels. If not, add the 'missing' labels and post a comment about adding missing labels. If the issue has all, post a comment that congratulates and gives more details about the project board

#### [lint-scss](GHA:-lint-scss)
- Checks and lints modified scss files in PRs

#### [move closed issues](GHA:-move-closed-issues)
- Moves a closed issue into either the QA or Done column of the project board. If the issue has a “hard” label (Feature: Refactor CSS, Feature: Refactor HTML, Feature: Refactor JS / Liquid, Feature: Refactor GH), the issue is moved to the Done column. If the issue has no “hard” labels but does have an “override” label (role: front end), the issue is moved to the QA column. If the issue has no “hard” or “override” labels and does have a “soft” label (role: back end/devOps, Feature: Analytics), it is moved to Done. All other issues are moved to QA

#### [pr instructions](GHA:-pr-instructions)
- Creates an instruction on how to get a copy of a PR branch for review, then uploads the results into an artifact

#### [pull request trigger](GHA:-pull-request-trigger)
- An open script that could be triggered when a pull request is closed on the following branches 'gh-pages', 'feature-homepage-launch', 'feature-tech-dropdown'

#### [set pr labels](GHA:-set-pr-labels)
- RegEx takes the issue number on the body of the PR, and uploads the results (including labels on the issue) into an artifact

#### [update team members](GHA:-update-team-members)
- Trim inactive members from the write team

#### [vrms data](GHA:-vrms-data)
- Generates a new vrms_data.json and commits that to the repository

#### [wr pr instructions](GHA:-wr-pr-instructions)
- Leaves a comment on new PRs with a link to the relevant documentation for reviewing PRs and the command line instructions for pulling down a new branch for review.

#### [wr pull request trigger](GHA:-wr-pull-request-trigger)
- An open script that should house all the other scripts (workflows) that should be triggered when a pull request is closed.

#### [wr set pr labels](GHA:-wr-set-pr-labels)
- This workflow is triggered when workflow [Set PR labels] is completed. Downloads artifact for the completed workflow. Then, gets the PR and issue number from the downloaded artifact and uses an API request to get the labels. Lastly, puts the same labels into the PR.

### Deprecated GHAs

#### [no-labels-template.md](https://github.com/hackforla/website/issues/2898)
- Removed the no-labels-template.md file so that the total number of bot comments are reduced, and developers would have less notifications. Edited lines 47-55 in post-labels-comment.js so that no comment object was created when all the correct labels were added, and therefore no comment is posted. 

---


### extra folders or files with unknown workflows
* Supporting Files Folder: [trigger-schedule](https://github.com/hackforla/website/tree/gh-pages/github-actions/trigger-schedule) - folder has one file ```.gitkeep``` and its empty - The .gitkeep was likely added as a way of forcing git to track the new empty directory when the person who created the GHA began working on it. This is not a supported feature of git and now that there is content in the directory, there is no real need for the .gitkeep file
The commit message for the .gitkeep file is just “Create directory for gha refactor”

