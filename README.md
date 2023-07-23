# dup_hawk

🦅 A bot the looks for duplicate issues on a GitHub repo, created especially for competitive security reviews. 

# Getting Started
## Requirements

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - You'll know you did it right if you can run `git --version` and you see a response like `git version x.x.x`
- [Python](https://www.python.org/downloads/)
  - You'll know you've installed python right if you can run:
    - `python --version` or `python3 --version` and get an output like: `Python x.x.x`
- [pipx](https://pypa.github.io/pipx/installation/)
  - `pipx` is different from [pip](https://pypi.org/project/pip/)
  - You may have to close and re-open your terminal
  - You'll know you've installed it right if you can run:
    - `pipx --version` and see something like `x.x.x.x`

## Installation

### pipx

```
pipx install dup_hawk
```

### From Source

```
git clone https://github.com/Cyfrin/dup-hawk
cd dup-hawk
pip install . -e
```

## Quickstart 

```

```

# Tests

```
poetry run pytest
```

## Integration tests

```
poetry run pytest -m ""
```

## Specific tests with pdb and stdout

```
poetry run pytest -k "test_mark_duplicates_from_dfs" --pdb -s
```