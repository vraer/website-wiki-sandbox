---
title: Link projects to Project pages
tags:
    - 'decision record'
    - 'adopted'
---


#### Issue

[Comment](https://github.com/hackforla/website/issues/2485#issuecomment-1261579356) on [#2485](https://github.com/hackforla/website/issues/2485)

#### Problem Statement

Per comment, it was proposed that a list of "good second issues" be made to add the hyperlinks to each of the projects in the .md files. Before this issue's linked pull request, the project names on the mini cards led to their hackforla.org/projects/.. page. After the pull request was merged, the project names led to their respective hackforla github pages.

#### Adopted Solution

It was determined there was a more optimized solution. This issue was fixed by the method implemented in issue [#3592 Link projects in program areas page to project page](https://github.com/hackforla/website/issues/3592) and its linked [pull request](https://github.com/hackforla/website/pull/3692). This method involves the following:

```
# Get project's filename and assign it to a variable
# Link this variable with {{project.title}}
```

as followed by the [code](https://github.com/hackforla/website/pull/3692/files):

```
42 {% for project in site.projects %}
43     {% for project_program in project.program-area %}
44         {% if program_areas[1].program-area == project_program %}
45             {% assign project_relative_path = project.slug | prepend: "../projects/" %}
46             <li class="project-card-mini inline-list" id="{{project.identification}}">
47                 <img class="project-card-mini-image" src="{{project.image}}" alt="{{project.image_alt}}" />
48                 <a class="project-card-mini-title" href="{{ project_relative_path }}">{{project.title}}</a>
49             </li>
50         {% endif %}
51     {% endfor %}
52  {% endfor %}
```

The tag `.slug` converts the file's name into a string, and the tag `prepend: "../projects/"` links the variable to the relative path of the project file in the codebase. This variable is then linked with the `project.title` to link the project name in the program-areas page to the actual hackforla.org/projects/.. page. This is looped through all of the .md files in the _projects collection to link all of the projects to their appropriate pages.
