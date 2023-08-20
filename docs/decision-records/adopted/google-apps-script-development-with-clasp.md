---
title: Google Apps Script development with clasp
tags:
    - 'decision record'
    - 'adopted'
    - 'role: dev'
---

#### Issue

[#3722](https://github.com/hackforla/website/issues/3722)

#### Problem Statement

- The decision had been made to bring Google Apps Scripts into the website GitHub repository, resulting in issue [Add latest version of Google Apps Scripts to GitHub #3641](https://github.com/hackforla/website/issues/3641).  In the context of that issue, the suggestion to use clasp was made.
- The Apps Script CLI, or clasp, is an npm module with commands to create, edit, and deploy Apps Script projects locally.  For Hack for LA, its most useful commands would be clone, pull and push for transferring code modules between Google Drive and the local workstation, to facilitate local editing and committing of code.  The tool would provide an alternative to copying/pasting code between Google Drive and the local workstation, which may be feasible for work on our current small codebase, but will become unwieldy if the codebase grows.  

#### Feasibility Determination

- Use of clasp is feasible and will provide benefits especially for devs who prefer to edit code in their local IDE, and especially if the codebase were to grow.
- Use of clasp will create a larger learning curve and setup time for new devs, including installation of node.js, npm, clasp, @types/google-apps-script, clasp-env.
- It would be possible to combine clasp with other npm modules such as prettifier, ESLint, Babel and tsgas, to create a custom "build/deploy" module.

#### Summary  

- Create a new issue [#4134](https://github.com/hackforla/website/issues/4134) to document the new Google Apps Script development process.  
- Update existing wins development issues to refer to new wiki page.
