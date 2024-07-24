#%%
import logging
import dlt
from dlt.sources.helpers import requests
from dlt.destinations import filesystem, duckdb
import os

#%%
local_file_system = filesystem(
    bucket_url='/repro',
)
parquet_file_system = filesystem(
    bucket_url='s3://repro',
)

pipeline = dlt.pipeline(
    pipeline_name='repro_pipe',
    destination=parquet_file_system,
    dataset_name='repro',
)

data = []
data.append({'a': 1})

# Extract, normalize, and load the data
pipeline_run = pipeline.run(
    data, 
    table_name='repro',
    write_disposition={'disposition': 'merge', 'strategy':'scd2'},
)

logging.warning('-----------')
logging.warning('-----------')
logging.warning('-----------')
logging.warning('-----------')
logging.warning('s3 successful')
logging.warning('-----------')
logging.warning('-----------')
logging.warning('-----------')
logging.warning('-----------')
data = [ {'b': 2} ]
pipeline_local = dlt.pipeline(
    pipeline_name='repro_local_pipe',
    destination=local_file_system,
    # destination='duckdb',
    dataset_name='repro',
)
pipeline_run = pipeline_local.run(
    data, 
    table_name='repro',
    write_disposition={'disposition': 'merge', 'strategy':'scd2'},
)
logging.warning("finished local...")
# %%
