import sqlalchemy as sa
from sqlalchemy.engine.base import Engine

from pandasql import sqldf

def create_connection_postgre(
    server: str,
    database: str,
    username: str,
    password: str,
    port: int
) -> Engine:

    conn = f"postgresql+psycopg2://{username}:{password}@{server}:{port}/{database}"
    
    return sa.create_engine(conn)


def create_database(
    connection: Engine,
    database_name: str
) -> bool:
    
    query = f"""
        create database
            {database_name}
        with
            encoding = 'UTF8'
    """

    try:
        connection.execute(
            object=query
        )

        return True

    except:
        return False


def table_exists(
    connection: Engine,
    schema_name: str,
    table_name: str
) -> bool:

    query = f"""
        select to_regclass('{schema_name}.{table_name}');
    """

    df_tables = sqldf(
        query=query,
        db_uri=connection.url
    )

    return df_tables.to_regclass.iloc[0] is not None

