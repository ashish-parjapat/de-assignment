from sqlalchemy import create_engine
import clickhouse_connect

from pipeline.config import config


def get_postgres_engine():
    connection_string = (
        f"postgresql+psycopg2://"
        f"{config.postgres_user}:"
        f"{config.postgres_password}@"
        f"{config.postgres_host}:"
        f"{config.postgres_port}/"
        f"{config.postgres_db}"
    )

    # Temporary debug
    print(f"Postgres Connection: {connection_string}")

    return create_engine(connection_string)


def get_clickhouse_client():
    return clickhouse_connect.get_client(
        host=config.clickhouse_host,
        port=int(config.clickhouse_port),
        username=config.clickhouse_user,
        password=config.clickhouse_password,
        database=config.clickhouse_db,
        secure=False,
    )