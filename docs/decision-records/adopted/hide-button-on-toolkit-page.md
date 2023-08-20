---
title: Hide button on Toolkit page
tags:
    - 'decision record'
    - 'adopted'
    - 'role: dev'
---

#### Issue

[#3678](https://github.com/hackforla/website/issues/3678)

#### Problem Statement

Checking to see if the Suggest a guide button has been successfully hidden.

#### Potential Solution

Using Dockers to check to see if the button has been hidden and the button is still within toolkit.html

#### Feasibility Determination

The potential Solution is feasible as the button has been hidden. After reviewing the initial site on the local machine, the button is not displayed.
![image](https://user-images.githubusercontent.com/38971729/220494923-cb61f083-7648-4dac-995f-9e575a5e68a1.png)

[/pages/toolkit.html](https://github.com/hackforla/website/blob/262395c6b76fa0cc2ecc3a6c4d313e96dd1d2346/pages/toolkit.html#L62):

```html
62          <div class="suggest-guide-group">
63              <h2 class="external-resources-text title3">External Resources</h2>
64              <!-- The Suggest a resource button has been temporarily hidden until we figure out how this button will function after it's clicked. See issue #3678 for more details. -->
65              <button hidden class="btn btn-primary btn-md-narrow">Suggest a resource</button>
66          </div>
```

**Summary:**

As of Febuary 21st, 2023, the button has been successfully hidden and is not displayed currently.
