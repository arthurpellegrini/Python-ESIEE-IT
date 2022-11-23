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
        self.data = self.data[~self.data.Data.str.contains('method')]

        return self.data

    def details_connexion_mail(self, mail: str) -> DataFrame:
        return self.data.loc[self.data['Data'].str.contains(mail)]

    def details_connexion_room(self, room: str):
        pass


if __name__ == "__main__":

    dataBB = DataBB()
    dataBB.get_data("dataBB.log.txt")
    dataBB.data = dataBB.data.reset_index(drop=True)  # réinitialise les index du dataframe

    print(dataBB.data, dataBB.data.shape, dataBB.details_connexion_mail('jenyross@gmx.co.uk'))
