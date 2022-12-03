import pandas as pd
import matplotlib.pyplot as plt
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

    def num_salle_to_mail(self, prof_id: str):
        if "@" not in prof_id:
            all_log_prof = self.data.loc[self.data['Data'].str.contains(prof_id)]
            for i in range(all_log_prof.shape[0]):
                if 'is starting room' in all_log_prof.iat[i, 2]:
                    return all_log_prof.iat[i, 2].split(" ")[3]
        return prof_id

    def mail_to_num_salle(self, prof_id: str):
        if "@" in prof_id:
            all_log_prof = self.data.loc[self.data['Data'].str.contains(prof_id)]
            for i in range(all_log_prof.shape[0]):
                if 'is starting room' in all_log_prof.iat[i, 2]:
                    return all_log_prof.iat[i, 2].split(" ")[7]
        return prof_id

    def details_connexion_prof(self, prof_id: str, histogramme: bool) -> str:
        """
        Permet de récupérer les détails des connexions en fonction de l'identifiant d'un professeur.
        :param prof_id: correspond au mail ou au numéro de salle du prof
        :return: Une chaine de caractères qui contient les détails de connexion d'un professeur.
        """
        prof_id = self.num_salle_to_mail(prof_id)

        all_log_prof = self.data.loc[self.data['Data'].str.contains(prof_id)]  # contient toutes les actions d'un prof

        last_date = ""
        duree_journaliere = []
        dates = []

        start_room_time, left_room_time, output = "", "", ""
        for i in range(all_log_prof.shape[0]):

            if 'is starting room' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is starting room at " + all_log_prof.iat[
                    i, 1] + "\n"
                start_room_time = all_log_prof.iat[i, 1]

            if 'has left room' in all_log_prof.iat[i, 2]:

                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " has left room at " + all_log_prof.iat[i, 1] + "\n"
                left_room_time = all_log_prof.iat[i, 1]
                temps_travail = int(self.delta_time(start_room_time, left_room_time))
                output += "\tDurée connexion -> " + str(temps_travail) + " minutes\n"
                if last_date != all_log_prof.iat[i, 0]:
                    duree_journaliere.append(temps_travail)
                    dates.append(all_log_prof.iat[i, 0])
                else:
                    duree_journaliere[-1] += temps_travail
                last_date = all_log_prof.iat[i, 0]

            if 'is attempting to login' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is attempting to login at " + all_log_prof.iat[
                    i, 1] + "\n"

            if 'is joining room' in all_log_prof.iat[i, 2]:
                output += all_log_prof.iat[i, 0] + "\t" + prof_id + " is joining room at " + all_log_prof.iat[
                    i, 1] + "\n"

        if histogramme:
            fig, ax = plt.subplots(figsize=(6, 6))

            ax.bar(dates, duree_journaliere)
            n, bins, patches = ax.hist(dates)
            fig.autofmt_xdate()
            plt.xlabel('Dates')
            plt.xticks(rotation='vertical')
            plt.ylabel('Volume horaire (min)')
            plt.title('Volume horaire travaillé par jour de ' + prof_id)
            plt.grid(True)
            plt.show()

        return output

    def details_connexion_eleve(self, prof_id: str, histogramme: bool) -> str:
        prof_id = self.mail_to_num_salle(prof_id)
        all_log_prof = self.data.loc[self.data['Data'].str.contains(prof_id)]
        student_name, student_ip, student_join, student_left, prof_left, output = "", "", "", "", "", ""
        list_student = []  # étudiants n'ayant pas quitté la salle
        for i in range(all_log_prof.shape[0]):

            if 'is joining room' in all_log_prof.iat[i, 2] and "@" not in all_log_prof.iat[i, 2]:
                student_name = all_log_prof.iat[i, 2].split(" ")[3:5]
                if 'is' in student_name:
                    student_name.remove('is')
                student_name = ' '.join(student_name)

                output += all_log_prof.iat[i, 0] + "\t" + student_name + " is joining room at " + all_log_prof.iat[
                    i, 1] + "\n"
                student_join = all_log_prof.iat[i, 1]
                student_ip = all_log_prof.iat[i, 2].split(" ")[1]
                if student_name not in list_student:
                    list_student.append(student_name)

            if 'has left room' in all_log_prof.iat[i, 2] and student_ip in all_log_prof.iat[i, 2] and student_ip != "":
                student_left = all_log_prof.iat[i, 1]
                if prof_left != "" and int(self.delta_time(prof_left, student_left)) > 0:
                    output += all_log_prof.iat[i, 0] + "\t" + student_name + " has left room at " + all_log_prof.iat[
                        i, 1] + "\n"
                    output += "\tDurée connexion -> " + self.delta_time(student_join, student_left) + " minutes\n"
                if student_name in list_student:
                    list_student.remove(student_name)

            if 'has left room' in all_log_prof.iat[i, 2] and self.num_salle_to_mail(prof_id) in all_log_prof.iat[i, 2]:
                prof_left = all_log_prof.iat[i, 1]
                output += all_log_prof.iat[i, 0] + "\t" + "l'hôte has left room at " + all_log_prof.iat[i, 1] + "\n"
                for student in list_student:
                    output += "\t" + "étudiant partie avec la fermeture de la salle : " + student + "\n"
                    output += "\tDurée connexion -> " + self.delta_time(student_join,
                                                                        prof_left) + " minutes\n"
                list_student = []

        if histogramme:
            # pas trouvé
            pass

        return output


if __name__ == "__main__":
    dataBB = DataBB()
    dataBB.get_data("dataBB.log.txt")
    dataBB.data = dataBB.data.reset_index(drop=True)  # réinitialise les index du dataframe

    # print(dataBB.data, dataBB.data.shape)
    print(dataBB.details_connexion_prof("annina.liddell@gmail.com", True))  # fonctionnel
    print(dataBB.details_connexion_eleve("annina.liddell@gmail.com"))  # fonctionnel
    # details_prof = input("entrer le nom d'un prof ou l'identifiant de sa salle")

# annina.liddell@gmail.com ou ann-nth-vwr-8ng  => log
