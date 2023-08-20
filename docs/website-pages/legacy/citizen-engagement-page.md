# Citizen Engagement

### Purpose of page

* Allow volunteers to find projects based on the program area(s) they are interested in

### Technical details

* URL: <https://www.hackforla.org/citizen-engagement>
* GitHub locations (includes any relevant html, css, yml, md, js files)
  <!-- Format of links: [directory(s) and page](https://github.com/hackforla/website/blob/gh-pages/[directory(s) and page]) -->
  * [pages/citizen-engagement.html](https://github.com/hackforla/website/blob/gh-pages/pages/citizen-engagement.html): Current HTML file for the Citizen Engagement page
  * [_includes/program-area-pages-cards.html](https://github.com/hackforla/website/blob/gh-pages/_includes/program-area-pages-cards.html): HTML file that provides the layout/format for each card on the Citizen Engagement page
    * This file used to be called `citizen-engagement-cards.html`.
  * [_sass/components/_citizen_engagement.scss](https://github.com/hackforla/website/blob/gh-pages/_sass/components/_citizen_engagement.scss): Current SCSS file for the Citizen Engagement page
  * [assets/js/citizen-engagement.js](https://github.com/hackforla/website/blob/gh-pages/assets/js/citizen-engagement.js)
  * [_projects](https://github.com/hackforla/website/tree/gh-pages/_projects): The directory for each project's Markdown file, which contains
    * `program-area` field that designates which program area page a project should be on. For the Citizen Engagement page, only projects with

      ```
      program-area:
        - Citizen Engagement 
      ```

      and `visible: true` in their Markdown file are displayed on the Citizen Engagement webpage
    * program area detailed info (`problem`, `solution`, `impact`, `sdg`, `card-image-src`, `card-image-alt`, `sdg-image-src`, `sdg-image-alt`) that is displayed as Problem, Solution, Impact, and Sustainable Development Goal on the Citizen Engagement webpage. (**Note:** Not all of the projects have this information yet.)
* Wiki Architecture references (includes links to details about reusable components)
* Figma pages
  * [Current Pages](https://www.figma.com/file/0RRPy1Ph7HafI3qOITg0Mr/Hack-for-LA-Website?node-id=3464%3A0)
  *
* Issue Label:  ```P-Feature: Citizen Engagement```
  * [In Issues Tab](https://github.com/hackforla/website/issues?q=is%3Aopen+is%3Aissue+label%3A%22P-Feature%3A+Citizen+Engagement%22)
  * [On Project Board](https://github.com/hackforla/website/projects/7?card_filter_query=label%3A%22p-feature%3A+citizen+engagement%22)

### Content (sections and features)

* Current Projects

### Page screenshot (current version)

* Date Updated: 2023-02-27

* <details>
    <summary>Expand to see desktop view at 1440px width</summary>
    <img src="https://user-images.githubusercontent.com/122488603/221667561-6c46579a-d15e-43f9-a1aa-705066107455.png" alt="">

  </details>

* <details>
    <summary>Expand to see mobile view at 375px width with all cards collapsed</summary>
    <img src="https://user-images.githubusercontent.com/122488603/221668071-4703257f-de51-479c-851c-a1074f27c8bb.png" alt="">
  
  </details>

* <details>
    <summary>Expand to see mobile view at 375px width with one card expanded</summary>
    <img src="https://user-images.githubusercontent.com/122488603/221668188-9be4d492-6c52-4cb0-9dc0-8c36fde70eed.png" alt="">

  </details>
