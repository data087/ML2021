import numpy as np
import pandas as pd

datapath = "~/data/diagnosis.data"

original_data = pd.read_csv(datapath, sep = "\t")

print(original_data)
