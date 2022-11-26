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
        self.data = self.data[
            ~self.data.Data.str.contains('method')]  # retire du dataframe les log contenant les method

        return self.data

    def details_connexion_mail(self, mail: str) -> DataFrame:
        all_log_prof = self.data.loc[self.data['Data'].str.contains(mail)]  # contient toute les actions d'un prof
        all_log_prof.sort_values(by=['Date'])  # trie par la date
        i = 0
        while i < all_log_prof.shape[0]:
            if 'is starting room' in all_log_prof.iat[i, 2] or 'is joining room' in all_log_prof.iat[i, 2]:
                print(f" joining :  {'is joining room' in all_log_prof.iat[i, 2]}")
                # vérifier aussi quand elle rejoint sa room
                # print(f"is starting {all_log_prof.iat[i, 2]}, {i}")
                if 'has left room' in all_log_prof.iat[i+1, 2]:
                    print(f"date join : { all_log_prof.iat[i, 0]}, date left { all_log_prof.iat[i+1, 0]}")
                    print(f"heure join : { all_log_prof.iat[i, 1]}, heure left { all_log_prof.iat[i+1, 1]}")
                elif 'is starting room' in all_log_prof.iat[i+1, 2]:
                    print("l'hote n'a pas quitté proprement la salle, donnée invalide")
            i += 1
            # commencer à partir du 'is starting room', si il y a ensuite une ligne 'has left room'
            # faire le calcul du temps entre son entrée et sa sortie, sinon si ça atteint une nouvelle ligne avec
            # is starting room alors dire : l'hote n'a pas quitté proprement la salle, donnée invalide
        return all_log_prof

    def connexion_room(self, room):
        return self.data.loc[self.data['Data'].str.contains('is starting room ' + room)]
        # arriver à extraire le nom du prof à partir du log issues de la salle
        pass

    def tentative_connexion_prof(self, mail):
        """
        Affiche les tentatives de connexion qu'un prof à eu.
        :param mail: mail du prof
        :return: none
        """
        var = self.data.loc[self.data['Data'].str.contains(f'{mail} is attempting to login')]
        i = 0
        while i < var.shape[0]:
            print(f"{mail} a tenté de se connecter le : {var.iat[i, 0]} à : {var.iat[i, 1]}")
            i += 1

    def details_connexion_room(self, room: str):
        pass

    def details_connexion_student(self, student: str):
        return self.data.loc[self.data['Data'].str.contains(student)]


if __name__ == "__main__":
    dataBB = DataBB()
    dataBB.get_data("dataBB.log.txt")
    dataBB.data = dataBB.data.reset_index(drop=True)  # réinitialise les index du dataframe

    print(dataBB.data, dataBB.data.shape)
    print(dataBB.details_connexion_mail("annina.liddell@gmail.com"))
    dataBB.tentative_connexion_prof("annina.liddell@gmail.com")
    details_prof = input("entrer le nom d'un prof ou l'identifiant de sa salle")
    print(dataBB.details_connexion_mail(details_prof))

# On souhaite pouvoir rentrer l'email d'un prof ou le numéro de sa salle et obtenir le
# détail de ses connexions :
# tentative de connexion
# jour et heure avec durée de la connexion (entre l'entrée et la sortie) en minutes) jour par jour
# jenyross@gmx.co.uk has successfully logged in.
