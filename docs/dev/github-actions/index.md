# GitHub Actions

!!! warning "This page was created as a demonstration. Please remove this note after page content is edited."

GitHub Actions is a powerful tool that we use to automate various tasks in our repository. This section of the documentation provides an overview of our GitHub Actions setup.

## Workflows

Workflows are the foundation of GitHub Actions. They are YAML files that define the automated tasks we want to run. We have several workflows in our repository, each serving a specific purpose. These workflows are located in the [`website/.github/workflows`](https://github.com/hackforla/website/tree/9fd80225966fc26eecf50027ae91d13d07d751d2/.github/workflows) directory. You can learn more about each workflow in the [Workflows](./workflows.md) section.

## Scripts

In addition to workflows, we also use scripts to perform more complex tasks. These scripts are written in JavaScript and are used by our workflows to automate tasks such as labeling issues and pull requests, posting comments, and more. These scripts are located in the [`website/github-actions`](https://github.com/hackforla/website/tree/9fd80225966fc26eecf50027ae91d13d07d751d2/github-actions) directory. You can learn more about each script in the [Scripts](./scripts.md) section.

## Interactions

Our workflows and scripts are designed to work together to automate tasks in our repository. The [Interactions](./interactions.md) section provides specific examples of how they interact.
