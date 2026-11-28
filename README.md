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

## Configuration

```bash
cp .env.example .env
```

Fill in `.env`:

- `EXTENDED_USER_ACCESS_TOKEN`, `INSTAGRAM_USER_ID`: Instagram Graph API access.
- `POSTGRES_HOST`, `POSTGRES_PORT`: where Python reaches the database, normally `localhost` and `5432`.
- `POSTGRES_DATABASE`, `POSTGRES_USER`, `POSTGRES_PASSWORD`: your choice. Postgres applies them only when the volume is first created.

## Database

Postgres 17 runs in Docker. Install Docker with Compose.

Start:

```bash
docker compose up -d
```

Create the `posts` table (needed once per database; safe to run again):

```bash
uv run src/grabcode/create_table.py
```

Connect with `psql` inside the container:

```bash
docker compose exec db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'
```

Stop:

```bash
docker compose down
```

Data stays in the `pgdata` volume. `docker compose down -v` deletes it.

## Usage

With the database running and the table created, fetch from @grabfoodth and save:

```bash
uv run src/grabcode/insert.py
```

It fetches the latest post. A post already stored (same ID) is skipped, so running it again adds no duplicate.

To print the fetched JSON without saving it:

```bash
uv run src/grabcode/fetcher.py
```

## Tests

Tests need the database running. They use a separate `grabcode_test` database, which they empty, so your saved posts are untouched. No Instagram API calls are made.

Create it once:

```bash
docker compose exec db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE DATABASE grabcode_test"'
```

Run:

```bash
uv run pytest
```
