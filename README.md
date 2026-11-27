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

## Database

Postgres 17 runs in Docker. Install Docker with Compose, then set `POSTGRES_PASSWORD` in `.env` (see `.env.example`).

Start:

```bash
docker compose up -d
```

Connect with `psql` inside the container:

```bash
docker compose exec db psql -U pongpradk -d grabcode-alpha
```

Other clients: `localhost:5432`, database `grabcode-alpha`, user `pongpradk`, password from `.env`.

Stop:

```bash
docker compose down
```

Data stays in the `pgdata` volume. `docker compose down -v` deletes it.

## Usage

```bash
uv run src/grabcode/fetcher.py
```

Prints the latest 4 posts from @grabfoodth as JSON.

## Tests

```bash
uv run pytest
```
