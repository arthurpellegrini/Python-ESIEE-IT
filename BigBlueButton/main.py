import pandas as pd
from pandas import *


def get_data() -> DataFrame:
    cols_name = ["Date", "Heure", "Data"]
    data = pd.read_fwf("dataBB.log.txt", encoding="latin-1", usecols=[0, 1, 5], names=cols_name)
    data = data.drop_duplicates()

    # On enlève les données qui contiennent des method=GET ou method=PUSH car pas utiles pour le travail à effectuer.
    indexes = []
    for i in data['Data'].index:
        raw_data = data['Data'][i]
        if "method=" in raw_data:
            indexes.append(i)
        #PAS TERMINé à revoir
        elif "[ActiveJob]" or "[NotifyUserWaitingJob]" in raw_data:
            print("BEFORE", raw_data)
            raw_data = raw_data.replace("[ActiveJob]", "").replace("[NotifyUserWaitingJob]", "")
            print("AFTER", raw_data)
            data.replace(data['Data'][i], raw_data)

    data = data.drop(indexes)

    # Créer de nouvelles colonnes pour les ID

    return data


if __name__ == "__main__":
    dataBB = get_data()
    print(dataBB, dataBB.shape)
