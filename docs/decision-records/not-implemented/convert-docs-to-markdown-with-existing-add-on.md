---
title: Convert docs to markdown with existing add-on
tags:
    - 'decision record'
    - 'not implemented'
---

#### Issue

[#2978](https://github.com/hackforla/website/issues/2978)
[Guides Issue #10 Comment](https://github.com/hackforla/guides/issues/10#issuecomment-1066190743)

#### Problem Statement

Converting the guides in Google Docs to Markdown so that the Markdown can be used to display the guides on our website.

#### Potential Solution

Using an add-on called [Docs to Markdown](https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607) to automatically convert from Google Docs to Markdown language.

#### Feasibility Determination

This potential solution is not feasible because of the errors and bugs encountered.

Our team had been using an add-on called [Docs to Markdown](https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607) to automatically convert from Docs to MD but encountered bugs after the extension's latest update as detailed below.

##### Technology we had been working with

- Docs to Markdown - Free, open-source Drive add-on that converts a Google Doc to simple, readable Markdown or HTML. (Available in Google Workspace Marketplace)
- Link to Extension: <https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607>
- The next sections are also mentioned in this issue: <https://github.com/hackforla/guides/issues/10#issuecomment-1066190743>

##### Summary

As of January 8, 2022, the Docs to Markdown Converter released an update that removes error/warning messages called `reckless mode`.

However, a message as seen below still appears at the top of the converted MD file and there are more issues encountered (mentioned in the next section) after converting the document.

![image](https://user-images.githubusercontent.com/38295612/158080504-07773395-43b1-4427-9f2e-c69883a4723c.png)

##### Issues Encountered After Update

<details markdown> <summary> Images are not in the correct order </summary>

Expected Output
![right-order](https://user-images.githubusercontent.com/38295612/158072463-0497a1f4-88e7-4fe5-a22f-80eeed20f60c.png)

Actual Output
![wrong-order](https://user-images.githubusercontent.com/38295612/158072457-1fd97035-a67c-41a3-a221-780b91fa8edf.png)

</details>

<details markdown> <summary> Backslashes appear randomly in the file </summary>

![Screenshot 2022-03-12 174359](https://user-images.githubusercontent.com/38295612/158070915-a6937dde-5b84-46cc-b697-225b2b14021b.png)

</details>
