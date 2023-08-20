---
title: Implement logging system for HFLA GitHub Actions
tags:
    - 'decision record'
    - 'not implemented'
---

#### Issue

[#1445](https://github.com/hackforla/website/issues/1445)

#### Problem Statement

Creating a Github action to print out certain parts of the Github action logs (Name of action, date run, Name of jobs and the job logs except for the run code) in a text document to maintain a permanent record of the Github action logs.

#### Potential Solution

Using REST API to download job logs seemed to be the most promising avenue although large amount of data processing would need to be done to remove the Github action code from the logs and get the data in a more readable state.

#### Feasibility Determination

It was decided to close this issue due to it requiring a advanced skill set and needing a large amount of time while providing little perceived benefit as a result.
