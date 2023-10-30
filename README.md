![CI](https://github.com/benhid/unique-visitors/actions/workflows/ci.yml/badge.svg)
![Release](https://github.com/benhid/unique-visitors/actions/workflows/release.yml/badge.svg)

# Unique Visitors

Count the number of unique visitors to a website without compromising their privacy. Built using FastAPI and backed by PostgreSQL.

## Install and Setup 

### Docker

The application can be run locally with Docker Compose:

```sh
docker compose up
```

The service will be available at http://localhost:80.

### Manual Setup

Install the required dependencies in a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Ensure you set the `DATABASE_URL` environment variable to connect with your PostgreSQL database. For example:

```sh
export DATABASE_URL=postgresql+aiopg://user:password@localhost:5432/db
```

(Check out [postgresql/](postgresql/) for a quick way to spin up a PostgreSQL database with everything pre-configured in Docker.)

Then, start the server with the following command:

```sh
uvicorn app.main:app --host 0.0.0.0 --port 80
```

## API endpoints

The service exposes the following endpoints:

Endpoint | Method | Description
--- |--------| ---
`/` | `GET`  | Fetches the total number of unique visitors.
`/site_view` | `POST` | Increments the visitor count by one.
`/version` | `GET`  | Provides the current version of the service.
`/healthz` | `GET`  | Checks the service health; returns 200 OK if up.

Use `curl` to interact with the service:

Initially, the count is zero.

```sh
$ curl http://localhost
0
```

Increment the visitor count by one:

```sh
$ curl -X POST -H "User-Agent: Mozilla/5.0" http://localhost/site_view
$ curl http://localhost
1
```

Subsequent requests from the same user (same user ip, agent) are ignored:

```sh
$ curl -X POST -H "User-Agent: Mozilla/5.0" http://localhost/site_view
$ curl http://localhost
1
```

## Tests

Execute the unit tests using:

```sh
python -m unittest discover -s tests
```

Code style and formatting is enforced with [Ruff](https://github.com/astral-sh/ruff):

```sh
python -m pip install ruff
ruff format app tests
ruff --extend-select I --fix app tests
```

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more details.