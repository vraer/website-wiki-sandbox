## Summary
[get-project-data.js](https://github.com/hackforla/website/blob/gh-pages/github-actions/trigger-schedule/github-data/get-project-data.js) appends new project data to [github-data.json](https://github.com/hackforla/website/blob/gh-pages/_data/external/github-data.json) and commits that to the repository
### Scheduled
Scheduled to run everyday at 11:00am GMT (3am PST) via the [schedule-daily-1100.yml](https://github.com/hackforla/website/blob/gh-pages/.github/workflows/schedule-daily-1100.yml) workflow file
### Workflow
1. Retrieve old [github-data.json](https://github.com/hackforla/website/blob/gh-pages/_data/external/github-data.json)
2. Retrieve all tagged and untagged repos
3. For each repo:
    1. Retrieve:
      - id
      - name
      - languages
      - url
      - Issue Contributors
      - Issue Comment Contributors
      - Project Contributors
    2. Append data in format below:
```
  {
        id: repo.id,
        name: repo.name,
        languages: Object.keys(repoLanguages.data),
        repoEndpoint: repo.url,
        commitContributors: {
          data: commitContributors
        },
        issueComments: {
          data: issueCommentContributors
        },
        contributorsComplete: {
          data: projectContributors
        },
  }
```

### Supporting Files/Folders
* Supporting Files Folder 1: [github-data directory](https://github.com/hackforla/website/tree/gh-pages/github-actions/trigger-schedule/github-data)
* Data: [github-data.json](https://github.com/hackforla/website/blob/gh-pages/_data/external/github-data.json)
* Workflow File: [schedule-daily-1100.yml](https://github.com/hackforla/website/blob/gh-pages/.github/workflows/schedule-daily-1100.yml)
