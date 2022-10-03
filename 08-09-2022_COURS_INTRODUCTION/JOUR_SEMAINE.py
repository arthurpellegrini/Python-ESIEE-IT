import datetime

CONSTANTES = {"SIECLES": {16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4},
              "VALEURS_MOIS": {"Janvier": 0, "Février": 3, "Mars": 3, "Avril": 6, "Mai": 1, "Juin": 4,
                               "Juillet": 6, "Août": 2, "Septembre": 5, "Octobre": 0, "Novembre": 3, "Décembre": 5},
              "JOURS_SEMAINE": ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
              }


def jour_semaine(num_jour: int, num_mois: int, num_annee: int) -> str:
    """
    Cette fonction permet de trouver le jour de la semaine à l'aide d'une date.
    :param num_jour: le numéro du jour.
    :param num_mois: le numéro du mois.
    :param num_annee: le numéro de l'année.
    :return: le jour de la semaine correspondant à la date fournie en paramètre.
    """
    valeur = num_annee % 100 + (num_annee % 100 // 4) + num_jour + CONSTANTES["SIECLES"][num_annee // 100]

    # On stocke le nom du mois correspondant à la date
    mois = list(CONSTANTES["VALEURS_MOIS"].keys())[num_mois - 1]

    # On ajoute la valeur correspondante au nom du mois
    valeur += CONSTANTES["VALEURS_MOIS"][mois]

    # Vérification Année Bissextile et janvier/février
    if (num_annee % 4 == 0 and num_annee % 100 != 0 or num_annee % 400 == 0) and (num_mois == 1 or num_mois == 2):
        valeur -= 1

    return CONSTANTES["JOURS_SEMAINE"][valeur % 7]


def enter_date_and_say_the_day() -> tuple[str, str]:
    """
    Cette fonction permet à l'utilisateur de rentrer une date valide, puis de donner le jour de la semaine correspondant
    à cette date.
    :return: la date sélectionnée par l'utilisateur.
    """
    is_not_valid_date = True

    # Tant que la date n'est pas valide, le programme continue à demander à l'utilisateur une nouvelle date
    while is_not_valid_date:
        date = input("Donnez moi une date (au format JJ/MM/AAAA): ")

        try:
            # S'il y a plus de 2 '/' dans la date
            if date.count("/") != 2:
                raise Exception

            # On découpe la chaîne de caractères afin de récupérer le jour, le mois et l'année de la date
            split_date = date.split("/")
            jour, mois, annee = int(split_date[0]), int(split_date[1]), int(split_date[2])

            # On vérifie la date du jour afin de savoir si celle-là est valide
            datetime.datetime(day=int(jour), month=int(mois), year=int(annee))

            # On vérifie que l'année n'est pas inférieur à 1600 ou supérieur à 2199 afin que l'année face partie des
            # siècles où l'on connaît la valeur correspondante
            if annee < 1600 or annee > 2199:
                raise Exception

            # Si aucune erreur n'est levée alors la date devient valide
            is_not_valid_date = False

        except Exception:
            print("La date n'est pas valide, veuillez respecter le format (JJ/MM/AAAA)")

    return date, jour_semaine(jour, mois, annee)


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    print("Le %s est un %s" % enter_date_and_say_the_day())
