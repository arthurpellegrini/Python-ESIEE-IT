import pandas as pd
from pandas import *


def get_data() -> DataFrame:
    cols_name = ["Date", "Heure", "Data"]
    data = pd.read_fwf("dataBB.log.txt", encoding="latin-1", usecols=[0, 1, 5], names=cols_name)
    data = data.drop_duplicates()

    # On enlève les données qui contiennent des method=GET ou method=PUSH car pas utiles pour le travail à effectuer.
    indexes = []
    for i in data['Data'].index:
        if "method=" in data['Data'][i]:
            indexes.append(i)

    data = data.drop(indexes)

    return data


if __name__ == "__main__":
    dataBB = get_data()
    print(dataBB, dataBB.shape)

