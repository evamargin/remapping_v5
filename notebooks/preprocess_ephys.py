# %% imports
import numpy as np
from pathlib import Path
import pandas as pd
from evabox import utils, ephys, plotting

# %% params
animal = "eb05"
date = "20251117"
params = utils.params_dict(animal, date)
print(params)

# %%
