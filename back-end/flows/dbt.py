from prefect import Flow
from prefect.storage import Module

# from flow_utilities.run_configs import docker_run_config
from prefect.run_configs import LocalRun

# import flows
from tasks.dbt import run_dbt, seed_dbt

# build the flow
FLOW_NAME = "run-dbt"

with Flow(
    FLOW_NAME,
    # schedule=None,
    # storage=Module("flows.dbt"),
    # run_config=LocalRun,
) as flow:
    seed = seed_dbt()
    task = run_dbt()

flow.run()
