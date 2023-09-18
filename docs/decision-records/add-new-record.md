# Adding new records

This guide provides step-by-step instructions for developers to create decision records.

## Adopted

!!! success "Solution Adopted"
    1. In the `adopted` directory, create a new markdown file for the decision record.
    2. Name the file using the format `<short-description>.md`, replacing `<short-description>` with a brief description of the decision. For example, `standardize-html-img-tag.md`
    3. Use the Decision Record Template provided below, and fill in the relevant information for your decision record.
    4. If you've added the tags correctly, the `hooks/page_links_by_tag.py` script will automatically add a markdown link to the new record in the appropriate list(s) on the website the next time the `mkdocs build` command is run.

    ``` markdown
    ---
    title: <Title in sentence case>
    tags:
        - 'decision record'
        - 'adopted'
        - 'role: <dev, design, research, general, etc.>'
    ---

    #### Issue
    
    #<issue_number>, #<issue_number_2> or None

    #### Problem Statement
    
    Explain the problem you're trying to solve in more detail.

    #### Potential Solution
    
    Describe the potential solution that was evaluated.

    #### Feasibility Determination
    
    Explain how the feasibility of the potential solution was determined, including any factors that influenced the decision (time, resources, etc.).

    #### Sources
    
    If applicable, include any relevant source links here.
    ```

## Not Implemented

!!! failure "Solution Not Implemented"
    1. In the `not-implemented` directory, create a new markdown file for the decision record.
    2. Name the file using the format `<short-description>.md`, replacing `<short-description>` with a brief description of the decision.
    3. Use the Decision Record Template provided below, and fill in the relevant information for your decision record.
    4. If you've added the tags correctly, the `hooks/page_links_by_tag.py` script will automatically add a markdown link to the new record in the appropriate list(s) on the website the next time the `mkdocs build` command is run.

    ``` markdown
    ---
    title: <Title in sentence case>
    tags:
        - 'decision record'
        - 'not implemented'
        - 'role: <dev, design, research, general, etc.>'
    ---

    #### Issue

    #<issue_number>, #<issue_number_2> or None

    #### Problem Statement

    Explain the problem you're trying to solve in more detail.

    #### Potential Solution

    Describe the potential solution that was evaluated.

    #### Feasibility Determination

    Explain how the feasibility of the potential solution was determined, including any factors that influenced the decision (time, resources, etc.).

    #### Sources

    If applicable, include any relevant source links here.
    ```
