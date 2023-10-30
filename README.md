# Unique Visitors

Count the number of unique visitors to a website without compromising their privacy.

## Install and Setup 

### Manual Setup

Install the required dependencies in a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

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

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more details.