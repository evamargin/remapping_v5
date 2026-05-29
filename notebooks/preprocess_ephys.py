# %%
%load_ext autoreload
%autoreload 2

# %% imports
import numpy as np
import pandas as pd
import yaml
import glob, os
from pathlib import Path
from evabox import utils, ephys

# %% input
animal = "eb08"
date = "20250425"

# %% params
paths = utils.build_paths(animal, date)
paths

#%% output folder
out_dir = paths['data_processed_ephys']
#%%
