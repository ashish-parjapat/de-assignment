#!/bin/sh

set -e

echo "Waiting for PostgreSQL..."

until python -c "
import psycopg2
psycopg2.connect(
    host='postgres',
    port=5432,
    user='${POSTGRES_USER}',
    password='${POSTGRES_PASSWORD}',
    dbname='${POSTGRES_DB}'
)
"
do
    sleep 2
done

echo "PostgreSQL is ready."

echo "Waiting for ClickHouse..."

until python -c "
import clickhouse_connect
client = clickhouse_connect.get_client(
    host='clickhouse',
    port=8123,
    username='${CLICKHOUSE_USER}',
    password='${CLICKHOUSE_PASSWORD}'
)
client.command('SELECT 1')
"
do
    sleep 2
done

echo "ClickHouse is ready."

exec python -m pipeline.run_pipeline