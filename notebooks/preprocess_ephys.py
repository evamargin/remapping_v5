# %%
%load_ext autoreload
%autoreload 2

# %% imports
import numpy as np
import pandas as pd
import yaml
from evabox import utils, ephys, plotting, preprocessing

# %% input
animal = "eb08"
date = "20260425"

# %% params
params = utils.params_dict(animal, date)
paths = utils.build_paths(params['animal'], params['date'])

# %%
periods = preprocessing.get_periods_df(
    params['animal'],
    params['date'],
    paths['data_processed_ttl'],
    params['ttl_type'],
    params['fs'],
    params['fsp']
)
periods
# %% savings
paths
# %% save stuff
out_dir = paths['results_session'] / "preprocessing"

utils.save_as_csv(periods, "periods", out_dir)
utils.save_as_yaml(params, "params", out_dir)
# %%
