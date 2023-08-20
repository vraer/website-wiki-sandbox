---
title: Standardize HTML img tag
tags:
    - 'decision record'
    - 'adopted'
    - 'role: dev'
---

#### Issue

None

#### Problem Statement

In our codebase, we are not consistent with whether we apply an ending slash for img HTML tags.

Example of code with `<img...>`:
<https://github.com/hackforla/website/blob/706d7ce3628f9958cda525201c7c444d3d57d21b/pages/404.html#L12>

Example of code with  `<img.../>`
<https://github.com/hackforla/website/blob/706d7ce3628f9958cda525201c7c444d3d57d21b/pages/donate.html#L18>

#### Potential Solution

Use the img HTML tag without an ending slash meaning <img...> (Source 1).

#### Feasibility Determination

This is feasible because we only use HTML. An ending slash in an img tag is needed for XHTML and XML (Source 2), which we don't use.

#### Sources

1. <https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element>
2. <https://stackoverflow.com/a/15149657>
