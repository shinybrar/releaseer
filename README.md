# Releaseer

This project aims to provide a walkthrough for best practices in release automation.

## Introduction

We use a set of tools and conventions to automate the release process. These tools and conventions are chosen to make the release process more efficient and less error-prone and work well with modern software development practices, such as Continuous Integration and Continuous Deployment (CI/CD). They build on top of each other to provide a seamless experience for developers, maintainers, and users. 

**At its core, this release process uses commit messages to determine the impact of a change in the codebase. It then uses this information to drive the release process, such as generating changelogs, creating release branches, and tagging releases and creating pull requests for maintainers to review.**

## Conventions and Specifications

The conventions and specifications used in this release process are agnostic to the programming language, framework, or platform. They are based on the current best practices in the industry and are designed to be flexible and extensible. They can be adapted to fit the needs of any specific project or development team.

- [Conventianal Commits](https://www.conventionalcommits.org/en/v1.0.0/), which is a specification for adding human and machine readable meaning to commit messages.
- [SemVer](https://semver.org), which is a specification for versioning software.
- [Changelog](https://keepachangelog.com/en/1.0.0/), which is a specification for maintaining the history of a project.
- [Continous Integration](https://en.wikipedia.org/wiki/Continuous_integration), which is a software development practice where developers integrate code into a shared repository frequently, preferably several times a day. Each integration can then be verified by an automated build and automated tests.
- Release Automation Process, which is the process of automating the release process. This can include automating the generation of changelog, the creation of release branches, the tagging of releases, and the publishing of releases.
- [Continous Deployment](https://en.wikipedia.org/wiki/Continuous_deployment), which is a software development practice where code releases automatically built, tested, and deployed to environments.

## Tools

To automate the release process, we use the following tools and practices which focus on developer experience, maintainability, and reliability. They are designed to be simple, efficient, and scalable with the goal of freeing developers from the burden of manual tasks and allowing them to focus on writing code.

- [Commitizen](https://commitizen-tools.github.io/commitizen/), which is a command-line tool for generating conventional commits. It provides a set of prompts for generating commit messages that follow the [Conventianal Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
- [Github Actions](https://github.com/features/actions), which is a Continuous Integration and Deployment platform provided by Github. It allows you to automate the release process by running scripts in response to events, such as pushing code to a repository or openning a pull request. You can use other CI/CD tools, such as Jenkins, Gitlab CI, and CircleCI as well.
- [Code Coverage](https://en.wikipedia.org/wiki/Code_coverage), which is a measure of how much of your codebase is covered by tests. It can be used to determine the quality of your tests and identify areas of your codebase that are not tested. You can use tools like `codecov`, `coveralls`, and `sonarqube` to measure code coverage. While code coverage is not a perfect measure of quality, it can still instill confidence in your codebase, especially in the paradigm of continuous integration and deployment.
- [Release Please](https://github.com/googleapis/release-please), which is a tool for automating the release process published by Google. It generates release PRs, changelog, and tags based on the Conventional Commits specification. It can be used as a standalone process or in conjunction with Github Actions to automate the release process.
- [Pre-commit](https://pre-commit.com), which is a framework for managing and maintaining multi-language hooks for git repositories. Hooks are scripts that run before or after certain git commands and can be used for a variety of tasks, such as linting, formatting, and testing. It can be used to enforce coding standards and conventions, such as commit message format. You can configure pre-commit to run `pytest` for a python project, `eslint` for a javascript project etc.

## Workflow

The workflow from making changes to the codebase to deploying the code to the production environment is as follows:

1. **Developer** either creates a feature branch or forks the main repository to make changes to the codebase.
2. **Developer** makes changes to the codebase and commits them using Commitizen to generate conventional commits.
3. **Developer** runs `pre-commit` locally to lint, format and optionally test the codebase.
4. **Developer** pushes the changes to their fork and opens a pull request to the main repository.
5. **Github Actions** runs the Continuous Integration process, which includes running tests, linting, and formatting the codebase to ensure it meets the project's standards. As projects mature, you can add more checks, such as security scans, performance tests, etc. to the CI process.
6. **Maintainer** reviews the pull request and merges it into the main branch of the source repository.
7. **Github Actions** runs detects the push to the main branch and runs the **replease-please** automation workflow. If the changes are determined to amount to a new release, i.e. a new feature, a fix, or a breaking change, a new release PR is created.
8. **Maintainer** reviews the release PR and merges it into the main branch of the source repository accumalating one or more downstream changes.
9. **Github Actions** runs the Continuous Deployment process, which includes building, testing, and deploying the codebase to the production environment. This includes generating the changelog, creating the release branch, tagging the release, and publishing the release as well as deploying the codebase to the production environment, e.g. kubernetes cluster, serverless environment, etc.

The following diagram illustrates the workflow:

```mermaid
%%{init: { 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'showBranches': true }} }%%
gitGraph
   commit
   commit tag: "v1.1.0"
   branch john/main
    commit
    commit
   checkout main
   branch jane/main
   checkout main
   merge john/main id:"bugfix"
    commit id: "Release Automation" type: HIGHLIGHT
   branch chore/release
    commit id: "v1.1.0"
   checkout jane/main
    commit id: "Clone Fork" type: HIGHLIGHT
    commit id: "Pre-Commit Setup" type: HIGHLIGHT
    commit id: "Make Changes and Commit" type: HIGHLIGHT
    commit
    commit
    commit id: "Push Changes to Fork" type: HIGHLIGHT
    commit id: "Open Pull Request" type: HIGHLIGHT
   checkout main
    commit id: "Run CI Process" type: HIGHLIGHT
    commit id: "Review and Merge PR" type: HIGHLIGHT
   merge jane/main id:"feature"
    commit id: "Run Release Automation" type: HIGHLIGHT
   checkout chore/release
    commit id: "v1.2.0"
   checkout main
    commit id: "Review and Merge Release PR" type: HIGHLIGHT
    merge chore/release tag: "v1.2.0"
    commit id: "Run CD Process" type: HIGHLIGHT
```

## Walkthrough

### Overview

`releaseer` is a python project, using next-gen tooling to manage a python project. These tools include:

- `uv`: An extremely fast Python package and project manager, written in Rust.
- `ruff`: An extremely fast Python linter and code formatter, written in Rust.
- `litestar`: A Python web framework for building modern APIs and web applications.
- `pydantic`: A data validation and settings management using Python type annotations.

### Installation

```bash annotate
# Installation on MacOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Alternatively, you can also use `brew` to install `uv` on MacOS:
brew install uv

# Installation on Windows
curl -LsSf https://astral.sh/uv/install.sh | sh
```
