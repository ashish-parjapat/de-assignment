from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Config:
    postgres_host: str = os.getenv("POSTGRES_HOST")
    postgres_port: str = os.getenv("POSTGRES_PORT")
    postgres_db: str = os.getenv("POSTGRES_DB")
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")

    clickhouse_host: str = os.getenv("CLICKHOUSE_HOST")
    clickhouse_port: str = os.getenv("CLICKHOUSE_PORT")
    clickhouse_user: str = os.getenv("CLICKHOUSE_USER")
    clickhouse_password: str = os.getenv("CLICKHOUSE_PASSWORD")
    clickhouse_db: str = os.getenv("CLICKHOUSE_DB")


config = Config()