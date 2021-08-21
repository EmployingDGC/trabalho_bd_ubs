import sqlalchemy as sa
from sqlalchemy.engine.base import Engine

import datetime as dt

from pandasql import sqldf

import pandas as pd
import unidecode as ud

def create_connection_postgre(
    server: str,
    database: str,
    username: str,
    password: str,
    port: int
) -> Engine:

    conn = f"postgresql+psycopg2://{username}:{password}@{server}:{port}/{database}"
    
    return sa.create_engine(conn)


def table_exists(
    connection,
    schema_name,
    table_name
):
    query = f"""
        select to_regclass('{schema_name}.{table_name}');
    """

    df_tables = sqldf(
        query=query,
        db_uri=connection.url
    )

    return df_tables.to_regclass.iloc[0] is not None

