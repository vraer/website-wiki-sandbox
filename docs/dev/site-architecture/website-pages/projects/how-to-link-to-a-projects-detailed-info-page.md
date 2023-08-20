# Link to project details

## Overview

The following instructions are for how to link to a project's detailed information page using:

* The filenames of the Markdown files in the `_projects` directory,
* [Liquid template language](https://shopify.github.io/liquid/), and
* [Jekyll](https://jekyllrb.com/).

We will be using code snippets from [this](https://github.com/hackforla/website/blob/2028efe03a4539f6f493bc47945783d0cbd8baaf/pages/program-areas.html) as an example. It is recommended to view the code snippets in the context of the code in order to understand it better.

## Instructions

1. Use a for loop to go through each file in the `_projects` directory using `site.projects`; something like `{%- for variable_name in site.projects -%}`.
    - From the example, see line 42: `{% for project in site.projects %}`
2. Create a variable with a relative pathname using Jekyll's `slug` attribute[^1] and using Liquid's `prepend` to prepend "../projects/"[^2]. `Slug` uses the filename of a document and "any character except numbers and letters is replaced as hyphen" in the filename[^1].
    - From the example, see line 45: `{% assign project_relative_path = project.slug | prepend: "../projects/" %}`
3. Use the relative pathname variable for the `href`.
    - From the example, see line 48: <br />
     `<a class="project-card-mini-title" href="{{ project_relative_path }}">{{project.title}}</a>`

## References

[^1]: See Jekyll's documentation on `slug` by searching for it on this webpage: [https://jekyllrb.com/docs/permalinks/#placeholders](https://jekyllrb.com/docs/permalinks/#placeholders)
[^2]: Liquid template language's `prepend`: [https://shopify.github.io/liquid/filters/prepend/](https://shopify.github.io/liquid/filters/prepend/)
