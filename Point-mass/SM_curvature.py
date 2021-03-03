## ==============================================================================
## www.speedmetrica.com
## ==============================================================================
## Calculating curvature from longitudinal speed and accelerations


## Importing libraries
import pandas as pd
import numpy as np
from pathlib import Path

## Setting the source signals as a dataframe

# choosing file
source_file = Path(Path.home(),'Github', 'lap-time-simulator', 'Point-mass', 'motec_exports', 'Interlagos_Ohira.csv')
source_df = pd.read_csv(source_file, error_bad_lines=False)

# Dropping null value columns out to avoid errors
source_df.dropna(inplace = True)

## disposable commands
print(print(source_df))





