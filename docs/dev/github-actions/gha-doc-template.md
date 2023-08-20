# {Action Name} (e.g., issue-trigger)

## Summary

Provide a brief overview of what this GitHub Action (GHA) does, its purpose, and any important context.

??? example
    This action is triggered whenever an issue is opened or reopened. It runs the `trigger-issue` scripts to check labels and post comments.

## Scheduled

- **Frequency**: Describe how often this action runs (e.g., daily, weekly).
- **Trigger Time**: Specify the exact time or conditions under which this action is triggered.

??? example
    - **Frequency**: Weekly
    - **Trigger Time**: Every Monday at 10:00 AM UTC

## Workflow Dependencies

List the workflows that are related to or dependent on this GHA. Include file names and links to the code if available.

??? example
    - `issue-trigger.yml`: [Link to the code](#)
    - `pull-request-trigger.yml`: [Link to the code](#)

## Supporting Files/Folders

Provide an overview of the supporting files and folders used by this GHA. Use a tree-like structure to show the hierarchy and relationships.

??? example

      ```bash
      .
      ├── check-labels.js
      ├── post-labels-comment.js
      └── add-preliminary-comment
          ├── check-label-preliminary-update.js
          ├── preliminary-update-comment.js
          └── preliminary-update.md
      ```

## Labels

List and describe any specific GitHub labels that are associated with this GHA, including how they are used within the workflow.

??? example
    - **label1**: Used to categorize issues.
    - **label2**: Used to assign priority.

## Test Procedure

Provide step-by-step instructions on how to test this GHA locally or in a specific environment. Include any necessary prerequisites, setup steps, and expected outcomes.

??? example
    - **Step 1**: Clone the repository and switch to the feature branch.
    - **Step 2**: Run the action using the provided test script.
    - ...

## Additional Notes (Optional)

Include any additional information, links to related documentation, caveats, or special considerations related to this GHA.

??? example
    Make sure to have the necessary environment variables set up before running the action.
