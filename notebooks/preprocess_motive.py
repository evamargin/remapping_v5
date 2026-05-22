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
paths = utils.build_paths(animal, date)
out_dir = paths['results_session'] / "preprocessing"

params = utils.load_yaml("params", out_dir)
# %% settings
max_gap = 10  # max NaN gap (frames) to interpolate; larger gaps stay NaN
pos_method = "cubic"  # position interpolation: 'linear', 'cubic', 'quadratic', 'akima'
# %%
