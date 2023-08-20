---
title: Explore local machine linters
tags:
    - 'decision record'
    - 'adopted'
    - 'role: dev'
---

#### Issue

[#2651](https://github.com/hackforla/website/issues/2651)

#### Problem Statement

Identifying a linter which can be installed locally so that developers can identify errors before making a PR.

#### Potential Solution

Having developers set up [ESLint](https://eslint.org/) on their local machines.

#### Feasibility Determination

In order to implement ESLint for standard use, all developers on the team (old and new) would have to individually install it on their local machines, which could be a bit to handle.

#### Summary

- Potential linters for use on developers' local machines were researched as requested by issue #2651 and ESLint was suggested as a possible solution, however a decision cannot be made until a spell checker for the repo is decided on so that we can determine compatability.
- If the decision to implement ESLint as the standard local linter were made, we would need to add the files it creates to the main repo; a package.json and .eslintrc.yml config file and we would also have to implement ESLint onto the repo with Github actions so that the repo linter matches everyone's local linter.
- A roll out plan would also need to be developed to ensure that everyone who is actively working and newly working on the website repo knows they need to implement ESLint on their local environments.
