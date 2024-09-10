# Software Release Walkthrough

Releaseer is a repository which provides **a walkthrough for releasing software.**

## Introduction

We use a set of tools and conventions to automate the release process. These tools and conventions are chosen to make the release process more efficient and less error-prone and work well with modern software development practices, such as Continuous Integration and Continuous Deployment (CI/CD). They build on top of each other to provide a seamless experience for developers, maintainers, and users. 

**At its core, this release process uses commit messages to determine the impact of a change in the codebase. It then uses this information to drive the release process, such as generating changelogs, creating release branches, and tagging releases and creating pull requests for maintainers to review.**

## Conventions and Specifications

- [Conventianal Commits](https://www.conventionalcommits.org/en/v1.0.0/), which is a specification for adding human and machine readable meaning to commit messages.
- [SemVer](https://semver.org), which is a specification for versioning software.
- [Changelog](https://keepachangelog.com/en/1.0.0/), which is a specification for maintaining the history of a project.
- [Continous Integration](https://en.wikipedia.org/wiki/Continuous_integration), which is a software development practice where developers integrate code into a shared repository frequently, preferably several times a day. Each integration can then be verified by an automated build and automated tests.
- Release Automation Process, which is the process of automating the release process. This can include automating the generation of changelog, the creation of release branches, the tagging of releases, and the publishing of releases.
- [Continous Deployment](https://en.wikipedia.org/wiki/Continuous_deployment), which is a software development practice where code releases automatically built, tested, and deployed to environments.

## Tools

To automate the release process, we use the following tools:

- [Commitizen](https://commitizen-tools.github.io/commitizen/), which is a command-line tool for generating conventional commits. It provides a set of prompts for generating commit messages that follow the [Conventianal Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
- [Github Actions](https://github.com/features/actions), which is a Continuous Integration and Deployment platform provided by Github. It allows you to automate the release process by running scripts in response to events, such as pushing code to a repository or openning a pull request. You can use other CI/CD tools, such as Jenkins, Gitlab CI, and CircleCI as well.
- [Release Please](https://github.com/googleapis/release-please), which is a tool for automating the release process published by Google. It generates release PRs, changelog, and tags based on the Conventional Commits specification. It can be used as a standalone process or in conjunction with Github Actions to automate the release process.
- [Pre-commit](https://pre-commit.com), which is a framework for managing and maintaining multi-language hooks for git repositories. Hooks are scripts that run before or after certain git commands and can be used for a variety of tasks, such as linting, formatting, and testing. It can be used to enforce coding standards and conventions, such as commit message format. You can configure pre-commit to run `pytest` for a python project, `eslint` for a javascript project etc.

## Releaseer

`releaseer` is a python project, using next-gen tooling, e.g.

- `uv`: An extremely fast Python package and project manager, written in Rust.
- `ruff`: An extremely fast Python linter and code formatter, written in Rust.

## Installation: `uv`

### MacOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternatively, you can also use `brew` to install `uv` on MacOS:

```bash
brew install uv
```

### Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | more"
```

## Installation: `releaseer`

```bash
uv sync
```

## Usage

```bash
uv run litestar --app releaseer.app:app run
```

