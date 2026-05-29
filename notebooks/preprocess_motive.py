# %%
%load_ext autoreload
%autoreload 2

# %% imports
import numpy as np
import pandas as pd
import yaml
import glob, os
from pathlib import Path
from evabox import utils, ephys, motive

# %% input
animal = "eb02"
date = "20250717"

# %% params
params = utils.params_dict(animal, date)
paths = utils.build_paths(params['animal'], params['date'])

#%%
paths

# %% ---------------parse MOTIVE csv files for each subsession---------------

# %% csv-->pandas for each csv in the loop 
ddf=[]
files_csv = glob.glob(os.path.join(paths['data_raw_motive'], '*.csv'))

for file_path in files_csv:
    ddf.append(motive.csv2df(file_path))

# %% parse motive meta
meta_list = [] # list with dicts that store meta for every subsession
for table in ddf:
    meta_list.append(motive.get_meta(table))
# %%
parsed_dicts = []
for table in ddf:
    parsed_dicts.append(motive.parse_motive(table))

# %% save preprocessed files as hdf5

# --- derive the session id from the takes; assert all CSVs are one session ---
subsession_ids = [m["Take Name"] for m in meta_list]
sessions = {sid.rpartition("_")[0] for sid in subsession_ids}
assert len(sessions) == 1, f"CSVs span multiple sessions: {sessions}"
session = sessions.pop()                 # e.g. 'eb08_20260425'
animal  = session.split("_")[0]          # e.g. 'eb08'
# %%
# --- load the two google-sheet tabs (your existing utils.load_tab) ---
sessions_df    = utils.load_tab(animal, "Sessions")
subsessions_df = utils.load_tab(animal, "SubSessions")
# %%
# --- build the HDF5 file for this session ---
out_path = Path(paths["data_processed_motive"]) / f"{session}_motive.h5"
out_path.parent.mkdir(parents=True, exist_ok=True)

problems = motive.write_session_file(
    out_path, session,
    parsed_dicts, meta_list,        # the two parallel lists you just built
    sessions_df, subsessions_df,
    mode="w",                       # 'w' = fresh build; 'a' = add subsessions to existing file
)
# %%
out_path = Path(paths["data_processed_motive"]) / f"{animal}_{date}_motive.h5"

motive.process_session_file(out_path, max_gap_frames=12)
save_dir = Path(paths["data_processed_motive"]) / "qc"
save_dir.parent.mkdir(parents=True, exist_ok=True)

motive.diagnose_session(out_path, save_dir=save_dir, euler_plots=True)
# %%
