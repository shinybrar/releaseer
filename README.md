# releaseer
Walkthrough for a software release from a commit through continuous integration & deployment.

## Requirements

`releaseer` is a python project, using next-gen tooling,

- `uv`: An extremely fast Python package and project manager, written in Rust.
- `ruff`: An extremely fast Python linter and code formatter, written in Rust.

To install `uv`, run the following command:

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