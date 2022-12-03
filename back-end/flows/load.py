from prefect import Flow

# import tasks
from tasks.download_data import download_data
from tasks.unzip_data import unzip_data
from tasks.truncate_data import truncate_data
from tasks.load_data import load_data

# build the flow
FLOW_NAME = "load-db"

with Flow(
    FLOW_NAME,
) as flow:

    # load tasks
    file_path = "data/landing/atl-crime_2022-10-20.zip"
    unzip = unzip_data(file_path=file_path)
    truncate = truncate_data(upstream_tasks=[unzip])
    load = load_data(upstream_tasks=[truncate])
