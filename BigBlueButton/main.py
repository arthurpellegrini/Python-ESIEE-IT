import pandas as pd

cols_name = ["Date", "Heure", "Data"]
dataBB = pd.read_fwf("dataBB.log.txt", encoding="latin-1", usecols=[0, 1, 5], names=cols_name)
dataBB = dataBB.drop_duplicates()
print(dataBB, dataBB.shape)

for i in dataBB['Data'].index:
    if "method=" in dataBB['Data'][i]:
        pass
        # dataBB = dataBB.drop(dataBB['Data'][i], inplace=True)


print(dataBB, dataBB.shape)
