---
title: Update GHA with Dependabot
tags:
    - 'decision record'
    - 'adopted'
---

#### Issue

[#2065](https://github.com/hackforla/website/pull/3414)

#### Problem Statement

Updating out-of-date dependencies of GHA using Github Dependabot.

#### Potential Solution

Our GHA are not latest version and hence we need to be notified when dependencies are out-of-date so that they don't break unexpectedly. The issue [#2065](https://github.com/hackforla/website/pull/3414) was created to check for updates to GHA at timed interval i.e. one week.

 But now Github Dependabot was updated to give out alerts for vulnerable GHA to stay up-to-date and fix security vulnerabilities in the actions
 workflow. It is powered by Github Advisory Database which will create an advisory to document the vulnerability when it is encountered in an
 action, triggering an alert for the impacted repository.

Pull requests raised by Dependabot to update dependencies is in accordance with how the repository is configured i.e., version updates and/or
 security updates and can be managed as other PRs but with extra commands which can be referred to [here](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates).

#### Feasibility Determination

Advantages for using GHA Dependabot:

- As Github Advisory Database powers Dependabot alerts for the impacted GH repository, so no additional action needs to be performed after Dependabot is enabled which has been done .
- Dependabot alert makes it easier to stay up-to-date and can be managed similar to other PRs ,thus eliminating the need for issue [#2065](https://github.com/hackforla/website/pull/3414).

Notes:
We need to configure a dependabot.yml file to have dependabot create pull requests. [Link to how to configure the file](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates). The issue to create the [file](https://github.com/hackforla/website/issues/3843)

Related Links:

- [Configuring dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates)
- [Managing pull requests for dependency updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates)
- [About dependabot alerts](https://github.blog/2022-08-09-dependabot-now-alerts-for-vulnerable-github-actions/#dependabot-alerts-for-github-actions)
