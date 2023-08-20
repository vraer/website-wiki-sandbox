---
title: Fix PR GitHub Actions bug with labels and instructions
tags:
    - 'decision record'
    - 'not implemented'
    - 'role: dev'
---

#### Issue

[#2933](https://github.com/hackforla/website/issues/2933)

#### Problem Statement

To squash the bug that is causing some PRs to not trigger the GitHub Actions(GHA) workflows for PR Labels and Instructions. Specifically for [#2918](https://github.com/hackforla/website/pull/2918) and [#2969](https://github.com/hackforla/website/pull/2969).

#### Potential Solution

Checking the labels every time the PR is "synchronized", which is triggered "when a pull request's head branch is updated. For example, when the head branch is updated from the base branch, when new commits are pushed to the head branch, or when the base branch is changed" ([source](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request)).

- because Lint SCSS did run and is triggered by the synchronized event

#### Feasibility Determination

Although the above could be a solution, I was not able to recreate the bug. In addition, the bug occurred within a 2 week period and has yet to occur again in 4 months. There's a possibility the bug has already been squashed.

Here's a summary of my findings.

- There are other reasons that labels aren't added by github-actions:
  - merge conflict (any on: pull_request workflows will not be triggered)
  - not merging into the specified branches (this can be found in the workflows .yml file)
    - for PR labels, it must be merging into gh-pages or feature-homepage-launch (Figure 1)
  - the PR creator added them during the creation of the PR
- In order to test GHA in your forked repository, you need to change your default branch to the branch you're working on (Figure 2)
  - because GHA only runs from the default branch
  - remember to change it back to gh-pages once you're done testing!
- For both issues that had the bug, there was another user's commit, although I have ruled that out in my testing.
  - if you plan on testing this, the commits were already merged before the PRs were created (and the merge is via squash and merge)
  - the steps that I used were: create new branch_1, make commits. create branch_2 from branch_1 (so that those edits are now in branch_2), make commits. make branch_1 PR, merge and squash. create branch_2 PR (there should be 2 commits).

If the bug comes up again, start to find the bug ASAP! Here are some tests to do.

- Check githubstatus.com to see if it's a GitHub problem, instead of a problem with our code
- Remove a label, and edit the PR to test if the workflow will run
- Contact the PR creator and talk to them

<details markdown><summary>Figure 1</summary>

![image](https://user-images.githubusercontent.com/31293603/199852407-56a82546-7a13-47ca-9253-b68fe618c487.png)
</details>
<details markdown><summary>Figure 2</summary>

![image](https://user-images.githubusercontent.com/86996158/179142211-04764947-c20a-4187-898a-d911d6f196f4.png)
</details>
