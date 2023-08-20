# Decision Records

This wiki page serves as the central hub for all decision records. Decision records help the team keep track of the decisions that have been made, along with the details and rationale behind them.

## Decision Record Workflow

See detailed instructions and templates for [adding new records](add-new-record.md):

- Create DR for [adopted solution](add-new-record.md#adopted)
- Create DR for [solution not implemented](add-new-record.md#not-implemented)

## Records Index

Links to records are generated on page build according to the  details specified in the yaml frontmatter for each markdown page. Query results can be modified as needed by altering the tags specified inside the HTML comments found in the source code below (e.g. generate list of records tagged per specific role, etc.).

### :green_square: Status: Adopted
<!-- TAGS='adopted' BEGIN -->
<details class="md-tag-details"><summary class="md-tag-summary">Tags</summary>
<p><a href="../../tags/#adopted" class="md-tag">adopted</a></p></details>

- [Standardize HTML img tag](adopted/standardize-html-img-tag.md)
- [Use merge commit for gh-pages updates](adopted/use-merge-commit-for-gh-pages-updates.md)
- [Link projects to Project pages](adopted/link-projects-to-project-pages.md)
- [Hide button on Toolkit page](adopted/hide-button-on-toolkit-page.md)
- [Update feature branches using merge commit](adopted/update-feature-branches-using-merge-commit.md)
- [Hand off issue follow-up by lead](adopted/hand-off-issue-follow-up-by-lead.md)
- [Update GHA with Dependabot](adopted/update-gha-with-dependabot.md)
- [Google Apps Script development with clasp](adopted/google-apps-script-development-with-clasp.md)
- [Explore local machine linters](adopted/explore-local-machine-linters.md)
<!-- TAGS END -->

### :red_square: Status: Not-implemented
<!-- TAGS='not implemented' BEGIN -->
<details class="md-tag-details"><summary class="md-tag-summary">Tags</summary>
<p><a href="../../tags/#not-implemented" class="md-tag">not implemented</a></p></details>

- [Convert docs to markdown with existing add-on](not-implemented/convert-docs-to-markdown-with-existing-add-on.md)
- [Maintain design system webpages](not-implemented/maintain-design-system-webpages.md)
- [Prevent liquid injection attacks in markdown](not-implemented/prevent-liquid-injection-attacks-in-markdown.md)
- [Capitalize menu items in nav bar and header](not-implemented/capitalize-menu-items-in-nav-bar-and-header.md)
- [Implement logging system for HFLA GitHub Actions](not-implemented/implement-logging-system-for-hfla-github-actions.md)
- [Receive project updates from PM](not-implemented/receive-project-updates-from-pm.md)
- [Fix PR GitHub Actions bug with labels and instructions](not-implemented/fix-pr-github-actions-bug-with-labels-and-instructions.md)
<!-- TAGS END -->
