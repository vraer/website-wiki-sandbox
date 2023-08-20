---
title: Update feature branches using merge commit
tags:
    - 'decision record'
    - 'adopted'
---

#### Issue

None

#### Problem Statement

Over time, feature branches become out of date with the code in the gh-pages branch. After updating the feature branch as outlined in steps [A. Updating a feature branch with changes from gh-pages](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch-with-changes-from-gh-pages#a-updating-a-feature-branch-with-changes-from-gh-pages) and [B. Opening a pull request](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch-with-changes-from-gh-pages#b-opening-a-pull-request) from [How to update a feature branch with changes from gh pages](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch-with-changes-from-gh-pages) wiki page, we need to figure out the best way to merge an "update the feature branch" pull request into the feature branch. (An "update the feature branch" pull request means a pull request that is opened for updating a feature branch with changes from gh-pages branch.)

#### Potential Solution

Merging an "update the feature branch" pull request into the feature branch using **"Create a merge commit"** option. For how to do it, see [D. (TECH LEADS ONLY) Merge the pull request into the feature branch with "Create a Merge Commit"](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch-with-changes-from-gh-pages#d-tech-leads-only-merge-the-pull-request-into-the-feature-branch-with-create-a-merge-commit) from [How to update a feature branch with changes from gh pages](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch-with-changes-from-gh-pages) wiki page.

#### Feasibility Determination

There are advantages and disadvantages of using **"Create a merge commit"** option when merging an "update the feature branch" pull request into the feature branch.
The disadvantages are:

- There will be two additional commits for each update:
  - INCLUDE WHAT THESE ARE AND WHERE THEY ARE FROM
  -

The advantages are:

- The history of contributors and commit ids for each individual file stays the same as the ones in gh-pages branch, which makes it easier to understand the code when trying to figure out the history of changes to a file.
- Eventually, when the feature branch is ready, the feature branch will be merged into the gh-pages branch. By using **"Create a merge commit"** to merge the pull requests to update the feature branch, any merge conflicts that were resolved will remain resolved, which isn't the case if "Squash and merge" was used.

Thus, the advantages outweigh the disadvantages, so the proposed solution to use **"Create a merge commit"** option when merging an "update the feature branch" pull request into the feature branch is the desired, feasible solution.
