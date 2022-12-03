from prefect import task


@task
def extract_data():
    """
    Extract data from a relational database as CSV files

    Parameters: None.

    Returns: None.
    """

    from utility.common import (
        create_db_connection,
    )

    from config.config import settings

    import pandas as pd

    from pathlib import Path

    try:

        conn = create_db_connection(
            settings.POSTGRES_USER,
            settings.POSTGRES_PASSWORD,
            settings.POSTGRES_HOST,
            settings.POSTGRES_PORT,
            settings.POSTGRES_DB,
        )

    except Exception as err:
        print(f"Unable to connect to the database.")
        print(err)

    try:

        # likely permissions issue resulting in empty dataframe
        query = f"select table_name as dataset from information_schema.tables where table_name like 'app_%' and table_schema = '{settings.DBT_SCHEMA}'"
        datasets = pd.read_sql(query, con=conn)

    except Exception as err:
        print("Unable to query a list of datasets.")
        print(err)

    try:

        # for index, row in datasets.iterrows():
        #     dataset = row["dataset"]
        datasets = ["app_cutoff", "app_map", "app_table"]
        for dataset in datasets:
            print(f"extracting dataset {dataset}")

            df = pd.read_sql(f"SELECT * FROM {settings.DBT_SCHEMA}.{dataset}", conn)
            df.to_csv(f"extracts/{dataset}.csv", index=False)

            print(f"Successfully extracted {settings.DBT_SCHEMA}.{dataset}.")

    except Exception as err:
        print(f"Unable to extract dataset {settings.DBT_SCHEMA}.{dataset}.")
        print(err)
