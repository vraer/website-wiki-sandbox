# Wins

## Current process for wins to appear on the wins page
- User fills out [share your wins form](https://docs.google.com/forms/d/e/1FAIpQLSeTiFjtxKbYgrJHAdFUovXlE55BdwwUQ9NePOXRY2q-h-w1tg/viewform) available through the `Share your wins` button on the [Wins page](https://www.hackforla.org/wins/) 
  - Form answers go onto the response tab of a spreadsheet automatically.
  - A Google Apps Script uses the access permissions of elizabethhonest bot account and creates an issue on the project board notifying us that the new submission needs to be reviewed
    <details>
    <summary>Screenshot of an issue created by the elizabethhonest bot account</summary>

    <img src="https://user-images.githubusercontent.com/37763229/158071517-0e074b14-11b1-4aa4-bb7a-d129d68cb6f1.png" width=450px>
    </details>

    - An `On form submit` trigger runs a function which reformats a copy of the answer from the response tab onto the review tab in the spreadsheet for review
    - Submission is reviewed by product (in the spreadsheet)
    <details>
    <summary>Screenshot of user response in review sheet</summary>

    ![image](https://user-images.githubusercontent.com/37763229/158071724-44f70f60-2a17-4daf-8b37-5617b90b4e6b.png)
    </details>

      - If acceptable, PM marks true for show on website
      - If exceptional, PM marks true for showing on about page (this functionality might not be fully implemented yet)
      - If not acceptable, PM marks false for show on website, so that it does not show on the website.  This is good for any spam.
- The Google Apps Script uses a `time-based trigger` to check the spreadsheet monthly and uses the access permissions of the elizabethhonest bot account to create a pull request for rows that should be added to the data in the json file.
- When the pull request is merged, the data in [_wins-data.json](https://github.com/hackforla/website/blob/gh-pages/_data/external/_wins-data.json) file gets updated and the [wins.js](https://github.com/hackforla/website/blob/gh-pages/assets/js/wins.js) file uses the json file to display the data on the [Wins page](https://www.hackforla.org/wins/). (Note: we are in the process of changing how the json files are generated, so this line item might need to be reviewed and updated again if required)
- Once a month, new wins might appear on the Wins page on website if the user entry is approved by PM and the related PR has been merged.

### [Automations for Wins page using Google Apps Script](Automations-for-Wins-page-using-Google-Apps-Script)

### [Steps for developers working on issues related to wins page](Steps-for-developers-working-on-issues-related-to-wins-page)

## Resources
**Note**: Permissions to some of these resources might be restricted due to involvement of user data, please reach out to leads for access requests. Also, the list of resources is not comprehensive for security reasons, but the Wins form admin guide has detailed information on what resources you might need. 
- [HfLA Website Admin Folder](https://drive.google.com/drive/folders/19ZHh3MTf4vmU9NPW1OViRQ4wvb8oGOoC)
- [Wins form admin guide](https://docs.google.com/document/d/1j1JTX5XzotgVCVZ91ImvenedPN5-IVjdSKDukq1B9iE/edit)
- [Share your wins form](https://docs.google.com/forms/d/e/1FAIpQLSeTiFjtxKbYgrJHAdFUovXlE55BdwwUQ9NePOXRY2q-h-w1tg/viewform)
- [_wins-data.json](https://github.com/hackforla/website/blob/gh-pages/_data/external/_wins-data.json) file 
- [wins.js](https://github.com/hackforla/website/blob/gh-pages/assets/js/wins.js) 
- [Wins page](https://www.hackforla.org/wins/)