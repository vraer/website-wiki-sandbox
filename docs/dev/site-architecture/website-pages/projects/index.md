# Projects

## Structure of the Project Cards and Project Pages

See the [index.html](https://github.com/hackforla/website/blob/gh-pages/pages/index.html) located in the root directory.
This is where all the sections (i.e. project cards, about, contact, etc.) of the home page are laid out. You'll see the following code:

``` js
---
permalink: /
---
{% assign remote-only = 'true' %}
{% if remote-only == 'false' %}
    {%- include hero.html -%}
    {%- include calendar.html -%}
    {%- include current-projects.html -%}
    {%- include press.html -%}
    {%- include about.html -%}
    {%- include forms/contact-us.html -%}
    {%- include sponsors.html -%}
{% else %}
    {%- include hero.html -%}
    {%- include home-getting-started.html -%}
    {%- include current-projects.html -%} 
    {%- include press.html -%} 
    {%- include about.html -%}
    {%- include forms/contact-us.html -%}
    {%- include sponsors.html -%}
{% endif %}   
```

All the items listed after `{%- include` are individual HTML files for each separate section, located in the [`includes` folder](https://github.com/hackforla/website/tree/gh-pages/_includes), which is standard in Jekyll.

If you follow the link to [current-projects.html](https://github.com/hackforla/website/blob/gh-pages/_includes/current-projects.html) in the `_includes` folder, you'll see that it contains a looping structure for displaying the project cards. The projects are sorted based on the front matter (by status and project name) determined in each individual project's markdown file located in the `_projects` folder.

- The primary level of sorting places the projects that are **Active** first, followed by **Rebooting**, **Completed**, and **On-Hold**, in this order.

- The secondary level of sorting is alphabetically by the projects' name, so projects are sorted alphabetically within each status group. For example, the ordering of projects would look like this:

    1. 311-Data (Status: Active)
    2. Civic Tech Index (Status: Active)
    3. Write for All (Status: Active)
    4. Food Oasis (Status: Rebooting)

Projects with the front matter `hide: true` will not appear on the home page.

Front matter/information for each project is located in the [_projects](https://github.com/hackforla/website/tree/gh-pages/_projects) folder. This folder contains the markdown files for each project. To update status, location, leadership, links, recruiting, and other information - simply edit the front matter (the information between the  `---`. This information will flow through to the project cards as well as the project pages. See the [Template of a project.md file](project.md-file-template) for more detail.

## Update logic, styling, and layout

### Project cards

To update logic, styling, and layout of ALL **project cards**, see the [project-card.html](https://github.com/hackforla/website/blob/gh-pages/_includes/project-card.html) in the _includes file. All the information extracted through the Liquid logic is coming from the markdown files in the `_projects` folder. Specifically, the following information is being extracted:
    * Project image link (actual images are stored in the [`asset\images\projects`](https://github.com/hackforla/website/tree/gh-pages/assets/images/projects) folder)
    * Project name and link to project page
    * Status of project
    * Project links (i.e. Github, website, Slack, etc.)
    * Project partner (if any)
    * Roles that the project is looking for (if the project is active or rebooting)
    * Project location, and
    * Technologies used for the project

### Project pages

To update the logic, styling, and layout of ALL **project pages**, see [`project.html`](https://github.com/hackforla/website/blob/gh-pages/_layouts/project.html) layout in the `_layout folder`. For a walk-through of the project layout, see the guide to the [project layout](project-layout.md) file.
