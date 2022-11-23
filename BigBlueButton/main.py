import pandas as pd
from pandas import *


class DataBB:
    def __init__(self):
        self.data = None

    def get_data(self, filename: str) -> DataFrame:
        """
        Cette fonction permet le prétraitement des données qui sont reçus en paramètres.
        """
        self.data = pd.read_fwf(filename, encoding="latin-1", usecols=[0, 1, 5], names=["Date", "Heure", "Data"])
        self.data = self.data.drop_duplicates()

        indexes = []
        for i in self.data['Data'].index:
            if "method=" in self.data['Data'][i]:
                indexes.append(i)
        return self.data.drop(indexes)

    def details_connexion_mail(self, mail: str) -> DataFrame:
        pass

    def details_connexion_room(self, room: str):
        pass


if __name__ == "__main__":
    dataBB = DataBB()
    dataBB.get_data("dataBB.log.txt")

    print(dataBB.data, dataBB.data.shape)
