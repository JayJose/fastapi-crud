from prefect import Flow

# import tasks
from tasks.extract_data import extract_data

# build the flow
FLOW_NAME = "extract-csvs"

with Flow(
    FLOW_NAME,
) as flow:

    # EXTRACT tasks
    extract = extract_data()
