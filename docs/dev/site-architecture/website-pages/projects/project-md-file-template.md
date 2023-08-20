# Project markdown file template

Use this to document a HFLA project.  
Entries are placed in the _projects/ folder. Jekyll pulls them into the cards on the [Projects](https://www.hackforla.org/#projects) section of the main page, and generates individual Project pages.

```yaml
---
# 'identification' is the 9 digit ID for your repo in the GitHub API.
# To find it, go to https://api.github.com/repos/<organizations>/<repository-name>
# For example, https://api.github.com/repos/hackforla/website
identification: ''
title:
description:
# card image should be 600px wide x 400px high
image: /assets/images/projects/[project repo name + .jpg or .png]
alt: 'description of the card image'
# hero image should be 1500px wide x 700px high
image-hero: /assets/images/projects/[project repo name + -hero + .jpg or .png]
leadership:
  - name: First Last
    role: Product Manager
    links:
      slack: 'https://hackforla.slack.com/team/xxxxxx'
      github: 'https://github.com/githubusername'
    picture: https://avatars.githubusercontent.com/githubusername
  - name: Given Surname
    role: Lead
    links:
      slack: 'https://hackforla.slack.com/team/xxxxxx'
      linkedin" 'https://linkedin.com/linkedin-username'
    picture: https://avatars.githubusercontent.com/githubusername
links: 
  - name: Github
    url: 'https://www.example.com'
  - name: Slack
    url: 'https://www.example.com'
  - name: Test Site
    url: 'https://test.example.com'
  - name: Demo Site
    url: 'https://demo.example.com'
  - name: Site
    url: 'https://live.example.com'
  - name: Overview
    url: https://github.com/hackforla/product-management/blob/master/project-one-sheets/[REPLACE WITH PROJECT NAME]-Project-One-Sheet.pdf
  # unused links can be commented out
  # - name: Showcase deck
  #   url: ''
  #   alt: ''
looking:
  - category: Development
    skill: one skill
  - category: UI/UX
    skill: another skill
  - category: Content
    skill: Researcher
technologies: 
  - Node.js 
  - ReactJS 
  - Ruby on Rails
  - other etc.
location: 
  - Downtown LA
  - Santa Monica
  - South LA
  # must choose one of the above (closest)
partner:
# Examples of tools are Figma, Photoshop, Sketch, Phone calls
tools:
# Add the necessary program area on the next line after the '-'
program-area:
  -
status:
# If the card should not be included on the site, change visible to "false"
visible: true
# If the project should not have a project homepage for any given reason, add the following line (uncommented):
# project-homepage: false
# For completed projects. Uncomment and add contact info if provided
# completed-contact:
# If the project has an iframe to link to a widget of their app, uncomment below and provide a source link (indents matter):
#iframe:
#  available: true
#  src: ""

# program area card data
# What problem this project addresses
problem: 
# How this project provides a solution to the problem
solution:
# The impact of this project 
impact: 
sdgs:
    # The Sustainable Development Goal (SDG) this project falls under (e.g. 9)
  - goal-number: 
    # The Sustainable Development Goal (SDG) target (e.g. b)
    target:
  - goal-number:
    target:
  - goal-number:
    target:
---
```

Data for the 'languages' and 'contributors' sections is pulled from the project's GitHub main repository using the GitHub API. In order to merge the GitHub API data into the finished card, you need to put the project's GitHub id in the 'identification field'. To find the id, go to the GitHub homepage for the project's main repository and search the page source for `<meta name="octolytics-dimension-repository_id" content="#####">`; the number in the 'content' field is the id you want.

If you cannot find the Github Repository ID refer to this [wiki article](https://github.com/hackforla/website/wiki/How-to-get-repository-ID-for-a-new-project-card)

[Sample](https://raw.githubusercontent.com/hackforla/website/gh-pages/_projects/311-data.md) project .md file for reference

[image naming decision record](https://github.com/hackforla/website/issues/233)

### Links

On the project homepage:

- Links with the names **GitHub**, **Site**, **Demo Site**, and **Test Site** displayed in the **Links** section in the left half of the Project Overview.
- Links named Wiki and Readme are displayed under the **Getting Started** dropdown
- All links are also displayed in the **Resources** section at the bottom of the project homepage

On the project card on HFLA homepage:

- All links are displayed

### Leadership

To create a Slack link for each person:

1. Go to the project's Slack channel.
2. Find a message from the person you want to create a link for.
3. Click on their name. This should give you a popup window with the user's picture, name, and a link to **View full profile**.
4. Click on **View full profile**.
5. That pane gives you the options message, call, and more.
6. Click on **more** and you should be shown **Copy member ID** followed by the actual id.
7. This is the id you need to use in the slack url, e.g. `https://app.slack.com/team/<member_id_here>`
