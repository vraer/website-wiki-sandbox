<!-- README: Style Guide -->
<!-- 
This wiki is formatted into two main sections: the *metadata*, and the *content*. This README, and directly below, is the *metadata*. These are not seen by visitors, but is there to utilize Markdown's limited programatic abilities.

Directly below the README are the Markdown reference-links, which are key, value pairs. The keys follow Python's convention for variable names. The first word of every key is always the linked website, followed by one or two words related to the link's content. Values are always links.

If the links are ever dead, for any reason, please only replace it from the Markdown Reference-links below and not further into the document.

The image links are not made into reference-links. Images might require resizing, so putting them in HTML <img> tags is more convenient for code maintanence purposes.

After the metadata, is the *content* of the Wiki. The style of every section is as such:

---

<a name="Title">

### Title

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 

[Return to top](#Top)

---

This pattern provides user-friendly navigation.

Likewise, most images are placed in dropdown using this format:

---

<details>
<summary>Title</summary>

<br>

> <img src="images/title-detail.png" width="" height="" />

<br>

</details>

---

This format prevents cluttering.

On the topic of images, the images lives in the 'images' directory, which is housed inside the wiki's repository. On Github's interface, the 'images' directory is invisible. To make changes to the directory, the wiki's repository must first be cloned locally.

When editting this wiki on the Github's interface, previews of the images are broken. This is normal, and is the result of using relative links as the source of the images. When not editting, the images should appear as normal.

The names of the images follow the format 'title of section'-'detail1'-'detail2'.

Also, images are marked using purple/orange rather than red because Github's green color scheme makes it hard for those with red-green blindness to discern the marks from Github's colors.

Note: The styles outlined in this README are not set in stone. They are only there to assist people who read and/or edit this Wiki. Should any of the styles no longer serve this purpose, feel free to perform edits as needed and update this README.

For more information on Markdown, visit: https://www.markdownguide.org/basic-syntax/ and https://guides.github.com/features/mastering-markdown/.
-->

<!-- Markdown Reference-links -->
<!-- "Different Ways of Leaving Feedback for a Collaborator" -->
[github_inline_comments]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request

<!-- "Step 1: Is there a linked issue?" -->
[github_issue_940]: https://github.com/hackforla/website/issues/940
[github_issue_1151]: https://github.com/hackforla/website/issues/1151
[github_issue_1326]: https://github.com/hackforla/website/issues/1326
[github_issue_1444]: https://github.com/hackforla/website/issues/1444
[github_linked_issue]: https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword

<!-- "Step 2: Understand the linked issue." -->
[wikipedia_rubberduck_debug]: https://en.wikipedia.org/wiki/Rubber_duck_debugging

<!-- "Step 3: View the changes in the browser." -->
[localhost_4000]: http://localhost:4000
[hackforla_homepage]: https://www.hackforla.org/
[chrome_developer]: https://developer.chrome.com/docs/devtools/device-mode
[microdoft_developer]: https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/device-mode
[firefox_developer]: https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode

<!-- "Documentation" -->
[github_review_doc]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/reviewing-changes-in-pull-requests
[h4la_figma]: https://www.figma.com/file/0RRPy1Ph7HafI3qOITg0Mr/Hack-for-LA-Website?node-id=2009%3A26149

<a name="Top"/>

| Table of Contents |
| ------------- |
| [Introduction](#Intro) |
| [Different Ways of Leaving Feedback for a Collaborator](#Feedback) |
| [How to Use Effective Communication in Your Feedback](#Comm) |
| [Step -1: Where do I find these Pull Requests You Speak of?](#Step-1)
| [Step 0: Is the pull request done with the correct branch?](#Step0) |
| [Step 1: Is there a linked issue?](#Step1) |
| [Step 2: Understand the linked issue.](#Step2) |
| [Step 3: View the changes in the browser.](#Step3) |
| [Step 4: Take a look at the source code.](#Step4) |
| [Step 5: Check for anything else.](#Step5) |
| [Step 6: Approve the pull request.](#Step6) |
| [Step 7: Clean up your working repo.](#Step7) |

| Supplementary Materials |
| ------------- |
| [The Do's and Don't's when Reviewing Pull Requests](#Reminders) |
| [Frequently Asked Questions](#Questions) |
| [Checklist](#Checklist) |
| [Sample Feedback](#Example) |
| [Flowchart*](#Brief) |
| [Documentation/Useful Links](#End)|

###### *For when you are familiar with the steps and only need a refresher

---

<a name="Intro"/>

## Introduction

Hi! Before we begin, allow me to thank you for taking your time to read this document! **Pull requests** are the heart and soul of the Hack for LA website project. By reviewing them, you ensure that the hackforla website is always up-to-date and provides a bug-free experience for our visitors.

As a member of the website team, you are expected to review pull requests. If the phrase, "pull request", inspires apprehension, worry not! This guide will equip you with the confidence you need to succeed at reviewing your first, and all subsequent, pull requests.

### What it means to review a pull request

When multiple collaborators –ahem– collaborate on a project, changes are constantly made. Because not all changes are desirable, the review process allows the team to intercept and assess changes before they are **merged** with the website.

The review process starts when a collaborator creates a **pull request**, a fancy word meaning, "I, the collaborator, have made changes, so please go over and approve them!". As a reviewer, your goal is to examine the website's appearance and source code following these changes. Specifically, you need to ensure the changes are: 1) *applicable*, 2) does not *break* the main website, and 3) *clean* (collectively know as the *ABCs*).

If the changes passes the *ABC's*, the pull request is **approved** for eventual merging with the website. Otherwise, you, as the reviewer, must leave feedback for the collaborator.

[Return to top](#Top)

<a name="Feedback"/>

## Different Ways of Leaving Feedback for a Collaborator

<details>
<summary>How to leave a comment or request changes</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/intro-comment-collab.png" width="" height="" />

<br>

</details>

When changes fail to follow any of the *ABC's*, there are a couple of ways to leave feedback for the collaborator: leave a comment, **request changes**, or leave an inline comment. As required, all three can be done at once, but one will often suffice.

### Leave a comment

This is usually reserved for clarification purposes. To leave a comment, go to the **Files changed** tab, if not already there. Then click the green button labeled, "Review Changes". In the pop-up, leave a comment, and be sure to select the "Comment" radio button before you submit. You can also use the @ shortcut to notify others to your comment.

### Request changes

When changes fail at least one of the *ABCs* criteria, the best way to leave feedback is to **request changes**. As the name implies, when you request changes, you detail additional steps the collaborator must take before their changes passes the *ABC's*. To request changes from a collaborator, select the "Request Changes" radio button rather than "Comment" radio button. This flags the pull request, preventing merges until a reviewer approve the additional changes. When requesting changes, be sure that they are specific and actionable!

### Leave an Inline Comment

<details>
<summary>How to leave feedback directly on code changes</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/intro-inline-review.png" width="" length="" />

<br>

</details>

When leaving a comment or requesting changes, you also have the option of commenting directly on the source code, through [Github's line comments feature][github_inline_comments]. If you have the time, I would encourage you to use inline comments as often as possible as they improve communication between reviewer and collaborator and minimize development time.

[Return to top](#Top)

<a name="Comm"/>

## How to Use Effective Communication in Your Feedback

* Do: Be specific when requesting changes. This helps the collaborator locate the necessary changes.
* Do: Be specific when giving praise. This reinforces excellence from one another and creates a positive environment. A "I like how readable your code is!" gives a lot more oxytocin than "Great job!"
* Do: Use language that you would use with a team member and a peer. That is, be courteous, be positive/encouraging, be clear, and be open/approachable.
* Do: Ask for input or help from other members of the team when relevant.

---

* Don't: Do the collaborator's work for them. Everyone is here to learn!

[Return to top](#Top)

<a name="Step-1"/>

## Step -1: Where do I find these Pull Requests You Speak of?

Pull requests for the website project can be found here: <https://github.com/hackforla/website/pulls>! When you are picking a pull request, the labels can help you decide which request to review. If this is your first review, pick a <code>Good: First Issue</code> before moving into <code>Good: Second Issue</code>, <code>Medium</code>, and <code>Large</code>. That said, there is no wrong way to pick a pull request to review. The most important thing is to try your best!

After picking a pull request to review and assigning yourself as a reviewer, add your review ETA and availability. Type this into the text field as a comment, then click the Comment button. The following is a sample comment to be added by a reviewer:

```
Review ETA: 6 PM 3/4/22
Availability: 5-8 PM Monday
```

When you have added your review ETA and availability, continue to Step 0.

<a name="Step0"/>

## Step 0: Is the pull request done with the correct branch?

<details>
<summary>Parts of a pull request's branch</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step0-branches.png" width="" length="" />

<br>

</details>

Before anything else, check that the pull request contains the correct branch. In other words, it must pass the following two checks:

* The commit *into* must be "hackforla:gh-pages"
* The commit *from* must be from the collaborator who opened the pulled request

If neither of the two criteria are met, then the collaborator might have made a mistake when making their pull request. Leave a comment stating that they have made the request with the incorrect branch and to redo the pull request with the correct branch.

[Return to top](#Top)

<a name="Step1"/>

## Step 1: Is there a linked issue?

<details>
<summary>Example of a linked issue</summary>

<br>

<img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step1-linkedissue.png" width="" height="" />

<br>

</details>

Every pull request comes with a post by the collaborator. Usually, a post contains: 1) a linked issue, 2) comments on the changes, and 3) screenshots of the changes. For this step, we will focus on the **linked issue**.

When a collaborator make changes, they implement them based on issues with the website. These issues are outlined in a separate post called a **linked issue**. Therefore, the linked issue provides important context that frames the collaborator's changes. Without it, there would be no way to tell whether changes are *applicable*!

Linked issues are usually in a *Word* #*number* (or in regex: [A-Za-z]*#\d*) format. They always link to a different post. Here are some, but not all, examples of a properly-formatted linked issue: Fixes [#940][github_issue_940], Fixed [#1151][github_issue_1151], Resolves [#1326][github_issue_1326], Closes [#1444][github_issue_1444].

If the linked issue is not in the correct format, the review can still proceed, but do leave a comment on [how to properly add a linked issue][github_linked_issue]. However, if the linked issue is missing, the review cannot proceed. Leave a comment for the collaborator to add a linked issue.

As an aside, we also ask that collaborators include before and after screenshots of their changes as part of the post. These images are there to help visualize the changes. If the images are not there, please gently remind the collaborator to include images before continuing with Step 2 of the review.

[Return to top](#Top)

<a name="Step2"/>

## Step 2: Understand the linked issue

<details>
<summary>Example of an issue</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step2-issue-comments.png" width="" length="" />

<br>

</details>

Before a reviewer can understand the collaborator's changes, they must first have an firm grasp on the **linked issue**. Visit the linked issue. Read the post and the comments below, visit all relevant links, and click on any dropdowns. Approach the issue with the goal of understanding the issue, so that, later, you may accurately assess the collaborator's changes.

A good way to test your understanding is to restate or summarize the issue in your own words (or to your [rubber duck][wikipedia_rubberduck_debug], if desired). This helps in finding gaps to your knowledge and prevents you from blindly reviewing changes you might not firmly understanding.

If after reading the linked issue, you find yourself confused, do not panic! This can arise from unclear wording, or unfamiliar jargon. At this point you have several options:

1. Research some of the unclear terms on your own
2. Consult the person who brought up the issue (through a comment or our slack)
3. Or, call on someone with more expertise (such as the person who wrote the issue) to review the issue with you

[Return to top](#Top)

<a name="Step3"/>

## Step 3: View the changes in the browser

The easiest way to view the collaborator's changes is to see them for yourself! Outlined below are steps to download the collaborator's branch into your own version of the website. Before creating a new branch in your repository, always sync your forked repo to the main repo. From your personal website fork on GitHub, click "Sync fork" at the right of the screen, then click "Update branch." You can also update your <code>gh-pages</code> branch by running <code>git pull</code> from the command line.

<details>
<summary>Example of how to sync your forked repo to the main repo</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step3-sync-demo.gif" width="" height="" />

<br>

</details>

<details>
<summary>Commandline instructions for Development Team</summary>

<br>

Type in these two commands into the repository, filling in for the variables inside of square brackets([ ]).

```
git checkout -b [nameOfCollaborator]-[nameOfFromBranch] [nameOfIntoBranch]
git pull https://github.com/[nameOfCollaborator]/website.git [nameOfFromBranch]
```

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step3-alternate-download-branch.png" width="" length="" />

<strong>nameOfIntoBranch</strong>: name of the branch from the website's repository (above sample is <strong><i>gh-pages</i></strong>)
<br>
<strong>nameOfCollaborator</strong>: the GitHub handle of the person doing the pull request (above sample is <strong><i>marcobarrera</i></strong>)
<br>
<strong>nameOfFromBranch</strong>: name of the branch that that belongs to the collaborator (above sample is <strong><i>update-footer-include-credits-page</i></strong>)
<hr>

</details>

<details>
<summary>Commandline instructions for Merge Team</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step3-download-branch.png" width="" length="" />

<br>

</details>

Once the branch is installed, run the website and [view it in the browser][localhost_4000]. You will also want to open [our website][hackforla_homepage] in a new tab. Locate the collaborator's changes on both sites and consider whether these changes address the issue. Some important questions to ask are:

1. Are the changes applicable to the issue?
2. Are there changes beyond those applicable to the issue?
3. Does the website appear less user-friendly?
4. Do the links and components on the page still work as intended?

In addition to viewing changes on your desktop browser, you must also assess these changes in multiple viewports (such as mobile or tablet), through your browser's developer mode.

<details>
<summary>An example of developer mode in Microsoft Edge (90.0.818.51)</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step3-devmode-edge.png" width="" height="" />

<br>

</details>

<details>
<summary>Links to developer mode documentation in popular browsers (bookmark this for future reference 😊)</summary>

1. [Google Chrome][chrome_developer]
2. [Microsoft Edge][microdoft_developer]
3. [Mozilla Firefox][firefox_developer]

</details>

After viewing these changes in your browser, you might discover that the changes are not *applicable* or *breaks* the website. In that case, you must **request changes**, and detail what exactly went wrong. If everything seems fine, you may proceed to Step 4.

[Return to top](#Top)

<a name="Step4"/>

## Step 4: Take a look at the source code

<details>
<summary>Changes in source code are marked in green/red or plus/minus</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step4-changes-code.png" width="" height="" />

<br>

</details>

At this step, you assess whether the changes are *applicable* and *clean*. Click the **Files changed** tab on the pull request page and examine the code. Green highlights (or lines with a plus sign) represent additions to the base website's code while red (or lines with a - sign) are deletions. Although *clean* is a subjective term, do make sure that the changes follow typical coding style guidelines. Good questions to ask are:

1. Can the changes be condensed?
2. Can the collaborator add comments to clarify any complex changes made?
3. Are there any drastic changes that seems like they do not belong?
4. Are there changes that are missing?

If something about the code is off, leave an inline comment and **request changes**.

[Return to top](#Top)

<a name="Step5"/>

## Step 5: Check for anything else

After viewing the changes in your browser and in the source code, the changes might still appear inadequate, erroneous, or incomplete. For example, the changes might have created an entirely new, unforeseen issue. Or there might have been a mistake in the original issue's wording which the collaborator did not caught. In such cases, leave a comment to discuss with the creator of the issue about your concerns. In some cases, you might also want the creator of the issue to review the pull request with you. Open the image below to see how to add them as a reviewer.

<details>
<summary>Manually adding another reviewer</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step5-adding-reviewer.png" width="" height="" />

<br>

</details>

[Return to top](#Top)

<a name="Step6"/>

## Step 6: Approve the pull request

<details>
<summary>How to approve a pull request</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/step6-comment-approve.png" width="" height="" />

<br>

</details>

If after going through all the steps, and you find all the changes passes the ABC's, then congratulations! We are ready to approve of these changes. To approve, visit the **Files changed** tab and click the green "Review changes" button on the top right. Select "Approve" and leave something nice for the collaborator. Something as simple as a, "Great job! I love what you have done, *insert name*!", will really make someone's day.

[Return to top](#Top)

<a name="Step7"/>

## Step 7: Clean up your working repo

In order to keep your working repo as clean as possible, it is best practice to delete the collaborator's branch after you submit your review. If you haven't already, return to your local branch using <code>git checkout gh-pages</code>, then run:

```
git branch -D name-of-collaborators-branch
```

This will help to reduce the likelihood of unwanted commits appearing in the future. Always delete the collaborator's branch as soon as your review is submitted. If you need to re-review the same PR later, create a new branch at that time.

[Return to top](#Top)

<a name="Reminders"/>

## The Do's and Don'ts when Reviewing Pull Requests

* Do: Check all files in the changed files tab.
* Do: Make sure all added/changed files are relevant to the issue.
* Do: When CSS changes, check a couple of pages rather than just the target page.
* Do: If changes are not apparent, try clearing the metadata first.
* Do: Leave encouraging, straightforward feedback.
* Do: Reward yourself! Reviewing code is not the easiest thing, so grab yourself a snack and try your best!

***

* Don't: Avoid reviewing pull requests.
* Don't: Be afraid to ask questions.
* Don't: Miss a step in this guide They are there for a reason!
* Don't: Merge the pull request, whether by accident (or malice, for that matter).

[Return to top](#Top)

<a name="Questions"/>

## Questions

<details>
<summary>1. Do I review a pull request if someone has already made a review? </summary>
<br>

>Yes! In fact, all pull requests require review by either 1 senior developer or 2 junior developers to merge. When reviewing a pull request with an existing review, be sure to check the previous review, so that you do not end up asking for the same changes.

<br>
</details>

<details>
<summary>2. After I request changes, do I need to review the pull request again after changes are made? </summary>
<br>

>As people lead busy lives, it can be difficult to keep track of and re-review a pull request, although we recommend you do so. It helps with our workflow, since, as the person who requested changes, you understand, more than others, the changes needed to be made.

<br>
</details>

<details>
<summary>3. Are there any limits to what pull requests I can review? </summary>
<br>

>Yes, we do have recommended guidelines for contributors when choosing which request to review. First, we recommend reviewing older rather than younger pull requests. Pull requests are usually done between issues, so it is better to let someone who had just finished an issue do a review as a break between issues. Other than that, we recommend reviewing pull requests that comes from <code>Good: First Issue</code> to start, before moving into <code>Good: Second Issue</code>, <code>Size: Small</code> or <code>Size: Medium</code> issues, and finally, <code>Size: Large</code> issues.

<br>
</details>

[Return to top](#Top)

<a name="Checklist"/>

## Checklist

* [ ] Step 0: Is the pull request done with the correct branch?
* [ ] Step 1: Is there a linked issue?
* [ ] Step 2: Understand the linked issue.
* [ ] Step 3: View the changes in the browser.
* [ ] Step 4: Take a look at files changed tab.
* [ ] Step 5: Check for anything else.
* [ ] Step 6: Approve the pull request.
* [ ] Step 7: Clean up your working repo.

[Return to top](#Top)

<a name="Example"/>

## Sample Feedback

<details>
<summary>Sample Feedback 1</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/sample-feedback-1.png" width="" height="" />

### Why this works

* Positive tone.
* Specific when requesting changes.
* Courteous.
* Appropriate language.

</details>

<details>
<summary>Sample Feedback 2</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/sample-feedback-2.png" width="" height="" />

### Why this works

* Encouraging tone.
* Specific when giving praise.
* Specific when requesting changes.
* Appropriate language.
* Ask for input from a member of the design team.

</details>

[Return to top](#Top)

<a name="Brief"/>

## Flowchart

<details>
<summary>Flowchart of Steps</summary>

<br>

> <img src="../../../legacy-docs/how-to/images/how-to-review-pull-requests/brief-flowchart.png" width="" length="" />

<br>

</details>

[Return to top](#Top)

<a name="End"/>

## Documentation

Github: [Reviewing changes in pull requests][github_review_doc]

HackForLA: [Figma][h4la_figma]

[Return to top](#Top)
