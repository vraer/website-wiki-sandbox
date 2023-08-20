# Template for tools

Use this to describe the attribution/credit for any tools used on the HfLA website that would go under the Tools section of the [Credits page](https://www.hackforla.org/credits/).  
Entries are placed in the [_data/internal/credits](https://github.com/hackforla/website/tree/gh-pages/_data/internal/credits) folder. Jekyll pulls them into the cards on the [Credits](https://www.hackforla.org/credits/) page.


```yaml
---
# The company, organization, or individual providing the tool
tool-provider:
# Please give the general site URL for the tool provider
provider-link:
# Location in our GitHub repo of the tool's logo
logo-url:
# The type of tool, such as a survey
tool-type:
# The area it is used in - Research, Development, Design, Product Management, etc
used-in: 
# A list of the project team(s) using the tool
used-by:
    # Name of a project team
  - project-name:
    # Link to the project team's page
    project-link:
    # Add additional project-name and project-link fields for each project team
  - project-name:
    project-link:
  - project-name:
    project-link:
---
```

[Sample] credit.yml file (Add a sample file when we have created one)

****