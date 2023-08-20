## A. Updating a feature branch with changes from gh-pages
### 1. Update your gh-pages on your forked remote repository by
   - Going to your forked repository and make sure you are on the gh-pages branch
   - Check your forked remote gh-pages branch is "...behind hackforla:gh-pages" or "This branch is up to date with hackforla/website:gh-pages."
     <details>
       <summary>Example of a forked remote gh-pages branch that is "...behind hackforla:gh-pages"</summary>
       <img width="960" src="https://user-images.githubusercontent.com/31293603/176553513-399f220a-5654-4714-8253-ce8e4f8cbaed.png">
     </details>
     <details>
       <summary>Example of a forked remote gh-pages branch that is "This branch is up to date with hackforla/website:gh-pages."</summary>
       <img src="https://user-images.githubusercontent.com/31293603/176553592-34310d50-fb6d-45b1-84d5-66b1cab22dce.png">
     </details>
     If it is "...ahead hackforla:gh-pages, you need to fix your forked remote gh-pages branch by re-forking hackforla/website repo. <b>You cannot proceed with the rest of the steps below until you fix your gh-pages branch.</b>
   - Click "Fetch upstream" and then the "Fetch and merge" button.
     <details>
       <summary>Animation showing clicking "Fetch upstream" and then the "Fetch and merge" button</summary>
       <img src="https://user-images.githubusercontent.com/31293603/176555221-84265c73-6717-4c92-8580-319384daddca.gif")
     </details>

### 2. In the terminal area in VS Code, navigate to the correct directory on your computer and then use the following commands to update your local gh-pages branch:
   - ```bash
     git checkout gh-pages
     ```
   - ```bash
     git status # To check there are no uncommitted files in your local gh-pages, so it should say, "nothing to commit, working tree clean"
     ```
   - ```bash
     git pull # To update your local gh-pages branch
     ```

### 3. The feature branch
#### 3.a. If you **don't** have the feature branch, create the feature branch locally and push it to your remote forked repo
   - Fetch the most recent changes on the upstream remote
     ```bash
     git fetch upstream
     ```
   - Then you need to create the local feature branch off of the upstream remote feature branch and then push it to your forked repo
     ```bash
     # example: git checkout -b feature-homepage-launch upstream/feature-homepage-launch
     # {FEATURE-BRANCH-NAME} needs to be identical to the feature branch name on the upstream remote repo
     git checkout -b {FEATURE-BRANCH-NAME} upstream/{FEATURE-BRANCH-NAME}
     git push --set-upstream origin {FEATURE-BRANCH-NAME}
     ```

#### 3.b. If you already have the feature branch, then you need to make sure your forked feature branch is in sync before proceeding to the next step by
   - Going to your forked repository and make sure you are on the feature branch
   - Check your forked remote feature branch is "...behind hackforla:{FEATURE-BRANCH-NAME}" or "This branch is up to date with hackforla/website:{FEATURE-BRANCH-NAME}", where {FEATURE-BRANCH-NAME} is the name of the feature branch
     <details>
       <summary>ADD IMAGE FOR THIS Example of a forked remote feature branch that is "...behind hackforla:..."</summary>

     </details>
     <details>
       <summary>Example of a forked remote feature branch that is "This branch is up to date with hackforla/website:...."</summary>
       <img alt="" src="https://user-images.githubusercontent.com/31293603/179347257-de390c5e-fa35-4d66-9e5e-b2735a3b815e.png">
     </details>
   - If it is "...ahead hackforla:{FEATURE-BRANCH-NAME}, you need to fix this problem by deleting the feature branch on your forked remote repo and locally on your computer, then do step [3.a If you **don't** have the feature branch, create the feature branch locally and push to your remote forked repo](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch-with-changes-from-gh-pages#3a-if-you-dont-have-the-feature-branch-create-the-feature-branch-locally-and-push-it-to-your-remote-forked-repo) above to create the feature branch again locally and push to your forked remote repo. **You cannot proceed with the rest of the steps below until you fix the feature branch.**
   - Click "Fetch upstream" and then the "Fetch and merge" button.
     <details>
       <summary>Animation showing clicking "Fetch upstream" and then the "Fetch and merge" button</summary>
       <img src="https://user-images.githubusercontent.com/31293603/176555221-84265c73-6717-4c92-8580-319384daddca.gif")
     </details>
   - In the terminal area in VS Code, navigate to the correct directory on your computer and then use the following commands to update your local feature branch:
   - ```bash
     git checkout {FEATURE-BRANCH-NAME} # where {FEATURE-BRANCH-NAME} is the name of the feature branch
     ```
   - ```bash
     git status # To check there are no uncommitted files in your local feature branch, so it should say, "nothing to commit, working tree clean"
     ```
   - ```bash
     git pull # To make your local feature branch in sync with the one in your remote forked repo
     ```

### 4. In the terminal area in VS Code on your computer, `docker-compose up` and familiarize yourself with how the website's various webpages look in the feature branch in various views (mobile, tablet, desktop) using developer tools. When done viewing the website using Docker, stop Docker using ctrl-c and then `docker-compose down`.
   - **Note:** Before you `docker-compose up`, I recommend deleting the `_site` directory in the root folder (website), deleting the `.jekyll-metadata` file in the root folder (website), and then clearing the cache in your browser. The reason is it makes sure that what you see visually when you `docker-compose up` is from the code from the feature branch and not from some previous code you were viewing.

### 5. Create your new branch off of the feature branch
   - ```bash
     # example: git checkout -b update-feature-homepage-launch-on-June-29-2022 feature-homepage-launch
     # Make sure your branch name includes what feature branch you are updating and the date you are doing the update
     git checkout -b {YOUR-BRANCH} {FEATURE-BRANCH-NAME} # {FEATURE-BRANCH-NAME} should be the name of the feature branch from step 3 above
     ```
   - Push your local branch to your remote repo.
     ```
     # {YOUR-BRANCH} is the name of the branch you just created
     git push --set-upstream origin {YOUR-BRANCH}
     ```
   - On your forked remote repo, compare the branch you just made and the feature branch on hackforla/website and they should be the same. To do this, 
     - Go to your forked remote repo
     - Click on "Pull requests"

     - Click on the "New pull request" button. (We are not going to make a pull request; we are just using the comparison feature.)

     - To do the comparison, set the following:
       - base repository: hackforla/website
       - base: {FEATURE-BRANCH-NAME}, where {FEATURE-BRANCH-NAME} is the name of the feature branch you want to update.
       - head repository: {YOUR-GITHUB-HANDLE}/website, where {YOUR-GITHUB-HANDLE} is your GitHub handle.
       - compare: {YOUR-BRANCH}, where {YOUR-BRANCH} is the branch you just created.
       The result should be "There isn’t anything to compare".

       <br>
       <details>
          <summary>Click here for an example of the settings and the desired result of the comparison</summary>
            This example uses
            <ul>
              <li>base repository: hackforla/website</li>
              <li>base: {FEATURE-BRANCH-NAME}, where {FEATURE-BRANCH-NAME} is feature-homepage-launch.</li>
              <li>head repository: {YOUR-GITHUB-HANDLE}/website, where {YOUR-GITHUB-HANDLE} is JessicaLucindaCheng.</li>
              <li>compare: {YOUR-BRANCH}, where {YOUR-BRANCH} is the branch update-feature-homepage-launch-on-June-29-2022.</li>
            </ul>
            <img src="https://user-images.githubusercontent.com/31293603/176592071-67147132-1b4c-40ef-bfd5-cee9f0589a81.png">
       </details>
     
### 6. Update the branch you just created with gh-pages using the commands below:
   - ```bash
     git merge gh-pages # This merges gh-pages into your branch
     ```
   - If there are **no** merge conflicts, then you can push the updates to your remote forked repo using this command:
     ```bash
     git push
     ``` 
   - If there **are** any merge conflicts, you will see a warning message of "Automatic merge failed; fix conflicts and then commit the result." You will need to resolve these merge conflicts before continuing with the rest of the steps.
     <details>
        <summary>Click here to see an example of a merge conflict warning</summary>
        <img alt="" src="https://user-images.githubusercontent.com/31293603/179381325-9e6da323-9fca-4514-beab-56c5aa1fe08b.png">
     </details>  
     <details>
       <summary>Click here for some tips for resolving merge conflicts:</summary>
       <ul>
         <li>With the warning message, it should tell you which file(s) have merge conflicts.</li>
         <details>
           <summary>Click here to see an example of a file indicated with a merge conflict. (<b>Note:</b> Your merge conflict may list multiple files.)</summary>
           <img alt="" src="https://user-images.githubusercontent.com/31293603/179381384-2d84e6a2-8ba3-48f9-8193-c95d52367b48.png">
         </details>
         <li>After opening the file(s) with merge conflicts in VS Code, you will see merge conflicts highlighted in green and blue.
           <details>
             <summary>Click here to see an example of the green and blue merge conflict highlighting in VS Code</summary>
             <img alt="" src="https://user-images.githubusercontent.com/31293603/179381435-a832548c-f351-4882-a09a-031eff576ebb.png">
           </details>
           <b>Note:</b> While there are default options to select all of the green highlighted code, all of the blue highlighted code to resolve the merge conflict, or accept both, sometimes it's none of those options. In other words, sometimes to resolve the merge conflict correctly, it can be a mix of some of the code highlighted in green and some of the code highlighted in blue.
         <li>To help resolve the merge conflict and figure out what code is the correct code, you can</li>
           <ul>
             <li>On the GitHub website, go to the <a href="https://github.com/hackforla/website">hackforla/website</a> repo and take a look at the files with merge conflicts and the commit history of each file on both</li>
             <ul>
               <li>the gh-pages branch and</li>
               <li>the feature branch</li>
             </ul>
             <li>Do a comparison of the feature branch with gh-pages branch to see what prs are specific to the feature branch. To do this, here are the instructions:</li>
               <ul>
                 <li>On the GitHub website, go to the <a href="https://github.com/hackforla/website">hackforla/website</a> repo</li>
                 <li>Click on "Pull requests"</li>
                 <li>Click on "New pull request" button. (We are not going to actually make a pull request. Just use the comparison feature.)</li>
                 <li>To do the comparison, set the following:<li>
                   <ul>
                     <li>base: gh-pages</li>
                     <li>compare: {FEATURE-BRANCH-NAME}, where {FEATURE-BRANCH-NAME} is the name of the feature branch you want to update.</li>
                   </ul>
                 <li>The results should show all the commits and changed files on the feature branch that are different from gh-pages. This can help with figuring out which pull requests/commits are specific to the feature branch.</li>
                 <li><b>Note:</b> Any commits that start with "Merge branch `gh-pages` into..." or "Merge pull request #..." are from updating the feature branch with the latest changes from the gh-pages branch.</li>
                 <details>
                   <summary>Click here to see an example of a comparison between gh-pages and a feature branch</summary>
                   <img src="https://user-images.githubusercontent.com/31293603/179381683-f7e6c5c0-bd97-4960-a241-4234fff02a90.png" alt="">
                 </details>
               </ul>
           </ul>
     </details>

     - Once done with resolving the merge conflict(s), follow these steps:
       - Save each file you had to resolve a the merge conflict in
       - In the terminal section of VS Code, `docker-compose up`and check how the website's various pages look in various views (mobile, tablet, desktop) using developer tools to make sure everything looks okay. Pay special attention to any areas where you had to resolve merge conflicts. For example, if you had to resolve a merge conflict in a SCSS class, you should do a search of every HTML and other files that use that class and pay special attention to those webpages. 
       - Then, use the following commands in the terminal section in VS Code to push changes to your remote forked repo:
         - For each file that you had to resolve a merge conflict in,
           ```bash
           git add {NAME-OF-FILE} #{NAME-OF-FILE} is the name of each file that you had to resolve a merge conflict in
           ``` 
         - After adding each file that had a merge conflict,
           ```bash
           git commit # To commit your files.
           ```
         - A window will pop up with the default merge commit message. Close the window to accept the commit message as is.
         - ```bash
           git push # To push your forked remote repo
           ```  
## B. Opening a pull request
### 7. Open a pull request with the following settings:
     - **base repository:** hackforla/website
     - **base:** {FEATURE-BRANCH-NAME}, where {FEATURE-BRANCH-NAME} is the name of the feature branch you want to update.
     - **head repository:** {YOUR-GITHUB-HANDLE}/website, where {YOUR-GITHUB-HANDLE} is your GitHub handle
     - **compare:** {YOUR-BRANCH}, where {YOUR-BRANCH} is the branch you created before and just pushed to changes to in step [6. Update the branch you just created with gh-pages](https://github.com/hackforla/website/wiki/How-to-update-a-feature-branch#6-update-the-branch-you-just-created-with-gh-pages-using-the-commands-below).
   <details>
     <summary>Screenshot of an example where the feature branch is feature-homepage-launch</summary>
     <img alt="" src="https://user-images.githubusercontent.com/31293603/179375637-6ec839bc-b62e-4908-a370-d3e686a71724.png">
   </details>

   - Then, fill in the rest of pull request template (Fixes #, changes made, etc) as usual and click "Create Pull Request"
     <details>
       <summary>INSERT IMAGE HERE Screenshot of an example of a pull request opened for updating the feature branch feature-homepage-launch</summary>
     </details>

## C. Reviewing the pull request
### 8. For people reviewing the pull request, here are some tips:
  - It is recommended that you have updated a feature branch yourself in a previous issue before reviewing this pull request. If you haven't ever updated a feature branch before, then please do steps 1-6 above to familiarize yourself with how to do it, and then just read step 7 (because you don't  need to open a pull request but should know how it's done and what the settings are for it.)  
  - If you do not know what the website on the feature branch looks like or it has been a while since you have viewed changes to the feature branch, you need to follow steps 3-4 to familiarize yourself with what is on the feature branch.
  - After pulling the code from the pull request into your local computer, remember to `docker-compose up` to view the site. **Note:** Before you `docker-compose up`, I recommend deleting the `_site` directory in the root folder (website), deleting the `.jekyll-metadata` file in the root folder (website), and then clearing the cache in your browser. The reason is it makes sure that what you see visually when you `docker-compose up` is the updates/code from the pull request and not from some previous code you were viewing.
- UPDATE THIS SECTION FOR HOW TO USE THIS FOR REVIEWS !!!!!!!!!!!!!!!!!!! To do the comparison, set the following:
       - base repository: hackforla/website
       - base: {FEATURE-BRANCH-NAME}, where {FEATURE-BRANCH-NAME} is the name of the feature branch you want to update.
       - head repository: {YOUR-GITHUB-HANDLE}/website, where {YOUR-GITHUB-HANDLE} is your GitHub handle.
       - compare: {YOUR-BRANCH}, where {YOUR-BRANCH} is the branch you just created.
       The result should be "There isn’t anything to compare".

       <br>
       <details>
          <summary>Click here for an example of the settings and the desired result of the comparison</summary>
            This example uses
            <ul>
              <li>base repository: hackforla/website</li>
              <li>base: {FEATURE-BRANCH-NAME}, where {FEATURE-BRANCH-NAME} is feature-homepage-launch.</li>
              <li>head repository: {YOUR-GITHUB-HANDLE}/website, where {YOUR-GITHUB-HANDLE} is JessicaLucindaCheng.</li>
              <li>compare: {YOUR-BRANCH}, where {YOUR-BRANCH} is the branch update-feature-homepage-launch-on-June-29-2022.</li>
            </ul>
            <img src="https://user-images.githubusercontent.com/31293603/176592071-67147132-1b4c-40ef-bfd5-cee9f0589a81.png">
       </details>

## D. (TECH LEADS ONLY) Merge the pull request into the feature branch with "Create a Merge Commit"
9. Read the [DR: Use merge commit for updating a feature branch with gh pages](https://github.com/hackforla/website/wiki/DR:-Use-merge-commit-for-updating-a-feature-branch-with-gh-pages) wiki page.
10. After the "update a feature branch" pull request has been reviewed, to merge the pull request into the feature branch,
   - Go to https://github.com/hackforla/website
   - Click "Settings"
   - Then, scroll down to the "Pull Requests" section and check the box next to "Allow merge commits". Note: We are only enabling this temporarily for merging "update a feature branch" pull requests.
   - Navigate to the "update a feature branch" pull request and scroll down to the bottom of the pull request
   - Click on the dropdown arrow and select "Create a merge commit" option.
     <details>
       <summary>Click here to see a screenshot of how to select "Create a merge commit" option</summary>
       <img width="243" alt="create-a-commit-merge" src="https://user-images.githubusercontent.com/31293603/183454460-682c8a3a-6c90-46ec-bf2c-6e3277f15929.png">
     </details>
   - Then click "Merge pull request".
   - (Optional) Edit the commit message.
   - Then click "Confirm merge"
   - Once done merging the pull request, go back to "Settings"
   - Then, scroll down to the "Pull Requests" section and **uncheck** the box next to "Allow merge commits" because we want to make sure that most pull requests are not merged using that option.
