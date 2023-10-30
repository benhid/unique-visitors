# postgresql-hll

This is a docker image for PostgreSQL with the [postgresql-hll](https://github.com/citusdata/postgresql-hll) extension.

## Usage

Build the image:

```sh
docker build -t postgres-hll:16.0-alpine -f Dockerfile.postgres .
```

And run:

```sh
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres-hll:16.0-alpine
```
