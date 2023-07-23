# How it could look:

## GitHub app

<!-- You need two things:
1. Webhook server (to listen for GitHub issues)
2. GitHub app server (to run the duplication stuff)
    -->

## Setup
1. User installs the app 
2. They run this script 

# PyGithub

We rebuilt the [GitHub API](https://docs.github.com/en/rest) because the [PyGithub](https://github.com/PyGithub/PyGithub) seems to be out of date beyond repair. There is a chance I just jumped the gun, but personally it was very frustrating to use. 

## Tasks

1. Build an API that can take in a GitHub URL and get it's issues
2. Have the bot upload issues to OpenAI looking for duplicates
3. Have it mark those issues on GitHub as duplicates

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