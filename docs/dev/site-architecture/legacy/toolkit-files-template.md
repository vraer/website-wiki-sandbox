There are two types of resources that can be added to the [Toolkit](https://www.hackforla.org/#toolkit) section.
- Guides
- External Resources

***

### How to add a Guide to Toolkit page.  
Entries are placed in the _guide-pages. Jekyll pulls them into the cards on the [Toolkit](https://www.hackforla.org/#toolkit) section of the main page, and generates individual guide pages.

```yaml
---
#name file as guide-name.html

title: 
#if description is >210 characters, short description will be used. Keep the short description under 210 characters.
description: 
short-description:
card-type: guide-page
#types of status: work-in-progress, depreciated, completed
status: 
display: true
#types of practice areas: Development, Design, Project Management, Professional Development
practice-area: 
tools: 
  - 
contributors: 
  - 
#types of sources: Hack for LA, Code for America, Other
source: 
recommended-by: 
#default svg is 'svg/default.svg'
svg: 
resource-url-completed: 
resource-url-wip:
resource-url-depreciated:
---
```
### Links
On the project card on Toolkit homepage:

* Title will be linked to resource-url-completed if guide status is 'completed'
* The "work in progress" text on the bottom right of the card will be linked to resource-url-wip if guide status is 'work-in-progress'


***
### How to add an External Resource to Toolkit page.  
Entries are placed in the _data/internal/toolkitresources.yml. Jekyll pulls them into the cards on the [Toolkit](https://www.hackforla.org/#toolkit) section of the main page, and generates individual External Resources pages.

```yaml
---
- title: 
  description: 
  card-type: 
  display: true
  #types of practice areas: Development, Design, Project Management, Professional Development
  practice-area: 
  tools:
    - 
  contributors:
  recommended-by: 
  svg: 
  resource-url: ''
---
```
### Links
On the project card on Toolkit homepage:

* Title will be linked to resource-url 
* As well as the bottom right icon
