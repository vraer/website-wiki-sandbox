---
title: Prevent liquid injection attacks in markdown
tags:
    - 'decision record'
    - 'not implemented'
    - 'role: dev'
---

#### Issue

[#3257](https://github.com/hackforla/website/issues/3257)

#### Problem Statement

Sanitizing project data by escaping HTML tags in the imported markdown for each project to prevent Liquid Injection attacks.

#### Potential Solution

Refactoring the project loading code in `assets/js/current-projects.js` to use regular expressions to escape HTML special characters before parsing the YAML into a JSON object rather than using liquid objects.

#### Feasibility Determination

It was decided that since some projects use HTML tags in their descriptions (namely line breaks) and since any malicious code added to a project's markdown file would have to be added by someone with access to the entire codebase anyway, this issue would not provide enough of a security benefit to be worth the restrictions it would place on project descriptions.
