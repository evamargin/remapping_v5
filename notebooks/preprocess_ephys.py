# %%
%load_ext autoreload
%autoreload 2

# %% imports
import numpy as np
import pandas as pd
from evabox import utils, ephys, plotting

# %% params
animal = "eb05"
date = "20251117"
params = utils.params_dict(animal, date)
print(params)

# %%
ttl_type = params['ttl_type']
paths = utils.build_paths(params['animal'], params['date'])
# %%
paths
# %%
ttl = ephys.load_binary(paths['raw_path'], channels=[384], n_channels=385)
ttl.shape
# %%
# TODO: check if Lans preprocessed merging actually includes ttl channel!