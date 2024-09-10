# Software Release Walkthrough

Releaseer is a sample repository, which provides **a walkthrough for releasing software.**

## Introduction

We use a set of tools and conventions to automate the release process. In no particular order, the tools and conventions are:

- [Conventianal Commits](https://www.conventionalcommits.org/en/v1.0.0/), which is a specification for adding human and machine readable meaning to commit messages.
- [SemVer](https://semver.org), which is a specification for versioning software.
- [Changelog](https://keepachangelog.com/en/1.0.0/), which is a specification for maintaining a changelog.
- [Release-Please](https://github.com/googleapis/release-please), which is a tool for automating the release process published by Google.

To enforce the conventions and specifications, we use the following tools:

- [Github Actions](https://github.com/features/actions), which is a Continuous Integration and Deployment platform provided by Github.
        - In theory, you can use any CI/CD tool, but we use Github Actions in this repository. Other popular tools include Jenkins, Gitlab CI, and CircleCI.
- [pre-commit](https://pre-commit.com), which is a framework for managing and maintaining multi-language hooks for git repositories. Hooks are scripts that run before or after certain git commands and can be used for a variety of tasks, such as linting, formatting, and testing.
- Finally any language specific tools you would like to use for linting, formatting, and testing.

## Releaseer

`releaseer` is a python project, using next-gen tooling, e.g.

- `uv`: An extremely fast Python package and project manager, written in Rust.
- `ruff`: An extremely fast Python linter and code formatter, written in Rust.

## Installation

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