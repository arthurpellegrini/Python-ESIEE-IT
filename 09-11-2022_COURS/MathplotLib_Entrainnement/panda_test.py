import pandas as pd

data = pd.read_excel("listeLignes.xlsx", usecols=[0, 2])
print(data.to_string())
