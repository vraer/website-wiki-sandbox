This guide describes how to set up a local branch while working off of a feature branch.



### Step 1: Create your branch
- Fetch the most recent changes on the upstream remote
    ```bash
    git fetch upstream
    ```
- Create the local branch off of the upstream remote branch
    ```bash
    # example: git checkout -b wins-feature-1 upstream/wins-feature-1
    # {FEATURE BRANCH NAME} needs to be identical to the feature branch name on the upstream remote repo
    git checkout -b {FEATURE BRANCH NAME} upstream/{FEATURE BRANCH NAME}
    ```

- Create your new branch off of the new feature branch that you just created!!
    ```bash
    git checkout -b {YOUR BRANCH}
    ```
### Step 2: Update your branch with upstream changes
- Update the branch with the latest changes using the following command
    ```bash
    # example: git pull upstream wins-feature-1
    git pull {NAME OF REMOTE} {FEATURE BRANCH NAME}
    ```
### Step 3: Create a pull request
- Stage and commit your changes
    ```bash
    git add {FILES CHANGED}
    git commit -m "{COMMIT MESSAGE}"
    ```
- Push changes to your remote
    ```bash
    # this is the same as always
    git push origin {YOUR BRANCH}
    ```
- Create a pull request that is comparing across forks, from your branch to the feature branch with the following settings:
  - **base repository:** hackforla/website
  - **base:** {FEATURE BRANCH NAME}, where {FEATURE BRANCH NAME} is the name of the feature branch you want to update.
  - **head repository:** {YOUR GITHUB HANDLE}/website, where {YOUR GITHUB HANLDE} is your GitHub handle
  - **compare:** {YOUR BRANCH}, where {YOUR BRANCH} is the branch you created in step 1
  <details>
    <summary>Screenshot of an example where the feature branch is feature-homepage-launch</summary>
    <img alt="" src="https://user-images.githubusercontent.com/31293603/179375637-6ec839bc-b62e-4908-a370-d3e686a71724.png">
  </details>

