import pyreadr
import pandas as pd

result = pyreadr.read_r("./TEP_FaultFree_Training.RData")   # read the RData file
print(result.keys())                        # shows all objects inside

# Example: load a dataframe
df = result[next(iter(result.keys()))]      # take first object
df.to_csv("output.csv", index=False)
print(df.head())
