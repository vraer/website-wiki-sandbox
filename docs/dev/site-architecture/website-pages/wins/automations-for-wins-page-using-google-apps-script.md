# Automations for Wins page using Google Apps Script

* As soon as a user submits the [share your wins form](https://docs.google.com/forms/d/e/1FAIpQLSeTiFjtxKbYgrJHAdFUovXlE55BdwwUQ9NePOXRY2q-h-w1tg/viewform), the `On form submit` triggers two functions:
     * The first function: Which grabs the data from the form and reformats it, and adds it to the same spreadsheet the form response goes to, but on another more readable tab (review)
          * Parses users' response using JSON.parse() 
          * Adds a timestamp to when the form was submitted
          * Formats the response to be used in our spreadsheet
          * Calls the Google App Script
          * Posts response to the review tab in the spreadsheet.
     * The second function:
          * Creates an issue to be added to our project board.
* The user's response will require an admin review to be considered for the Wins page.
* Next, a `time-based trigger` which triggers daily, in the same Google Apps Script, creates a Pull Request which if merged adds the new row (in the spreadsheet with a True value in the Display column) to the Wins page on the website.