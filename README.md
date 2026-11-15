# grabcode

Collects Grab discount codes from Instagram posts.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Python 3.12+

## Setup

```bash
git clone https://github.com/pongpradk/grabcode.git
cd grabcode
uv sync
```

`uv sync` creates `.venv` and installs the project and its dev dependencies.

## Usage

```bash
uv run src/grabcode/fetcher.py
```

Prints the latest 4 posts from @grabfoodth as JSON.

## Tests

```bash
uv run pytest
```
