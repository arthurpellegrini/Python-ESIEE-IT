import pandas as pd
from pandas import *
from datetime import datetime


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

    def delta_time(self, s1: str, s2: str) -> str:
        """
        Permet de récupérer la différence de temps entre ces deux horaires.
        :param s1: date de l'ouverture de la salle
        :param s2: date de fermeture de la salle
        :return: La différence en minutes des deux heures passées en paramètres.
        """
        formatting = '%H:%M:%S'
        delta = datetime.strptime(s2, formatting) - datetime.strptime(s1, formatting)
        return str(int(delta.total_seconds() / 60))

    def details_connexion_prof(self, prof_id: str) -> str:
        """
        Permet de récupérer les détails des connexions en fonction de l'identifiant d'un professeur.
        :param prof_id: correspond au mail ou au numéro de salle du prof
        :return: Une chaine de caractères qui contient les détails de connexion d'un professeur.
        """
        if "@" not in prof_id:
            all_log_prof = self.data.loc[
                self.data['Data'].str.contains(prof_id)]
            for i in range(all_log_prof.shape[0]):
                if 'is starting room' in all_log_prof.iat[i, 2]:
                    prof_id = all_log_prof.iat[0, 2].split(" ")[3]
                    break

        all_log_prof = self.data.loc[self.data['Data'].str.contains(prof_id)]  # contient toutes les actions d'un prof

        start_room_time, left_room_time, output = "", "", ""
        for i in range(all_log_prof.shape[0]):

            if 'is starting room' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is starting room at " + all_log_prof.iat[
                    i, 1] + "\n"
                start_room_time = all_log_prof.iat[i, 1]

            if 'has left room' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " has left room at " + all_log_prof.iat[i, 1] + "\n"
                left_room_time = all_log_prof.iat[i, 1]
                output += "\tDurée connexion -> " + self.delta_time(start_room_time, left_room_time) + " minutes\n"

            if 'is attempting to login' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is attempting to login at " + all_log_prof.iat[
                    i, 1] + "\n"

            if 'is joining room' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is joining room at " + all_log_prof.iat[
                    i, 1] + "\n"

        return output

    def details_connexion_eleve(self, room: str):
        # l'élève génère un left the room quand il part sinon on considère que lorsque le prof quitte la salle les élèves aussi

        # if 'is joining room' in all_log_prof.iat[i, 2]:
        #     output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is joining room at " + all_log_prof.iat[
        #         i, 1] + "\n"
        pass


if __name__ == "__main__":
    dataBB = DataBB()
    dataBB.get_data("dataBB.log.txt")
    dataBB.data = dataBB.data.reset_index(drop=True)  # réinitialise les index du dataframe

    # print(dataBB.data, dataBB.data.shape)
    print(dataBB.details_connexion_prof("annina.liddell@gmail.com"))  # fonctionnel
    # details_prof = input("entrer le nom d'un prof ou l'identifiant de sa salle")

# jenyross@gmx.co.uk => log pourrie  annina.liddell@gmail.com => log de qualité
