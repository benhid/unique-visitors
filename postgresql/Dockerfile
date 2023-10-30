FROM postgres:16.0-alpine AS builder

RUN apk --update add --no-cache wget build-base llvm15 clang15

WORKDIR /src

RUN wget https://github.com/citusdata/postgresql-hll/archive/refs/tags/v2.18.tar.gz -O postgresql-hll.tar.gz && \
    tar xf ./postgresql-hll.tar.gz

WORKDIR /src/postgresql-hll-2.18

RUN make &&  make install

FROM postgres:16.0-alpine

ENV POSTGRES_PASSWORD postgres

RUN echo "shared_preload_libraries = 'hll'" >> /usr/local/share/postgresql/postgresql.conf.sample
COPY hll_extension.sql /docker-entrypoint-initdb.d/
COPY --from=builder /src/postgresql-hll-2.18/*.sql /usr/local/share/postgresql/extension/
COPY --from=builder /src/postgresql-hll-2.18/*.control /usr/local/share/postgresql/extension/
COPY --from=builder /src/postgresql-hll-2.18/*.so /usr/local/lib/postgresql/