from prefect import Flow

# import tasks
from tasks.dbt import run_dbt, seed_dbt

# build the flow
FLOW_NAME = "transform-db"

with Flow(
    FLOW_NAME,
) as flow:

    # DBT tasks
    seed = seed_dbt()
    run = run_dbt()
