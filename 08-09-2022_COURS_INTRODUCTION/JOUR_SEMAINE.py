CONSTANTES = {"SIECLES": {16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4},
              "VALEURS_MOIS": {"Janvier": 0, "Février": 3, "Mars": 3, "Avril": 6, "Mai": 1, "Juin": 4,
                               "Juillet": 6, "Août": 2, "Septembre": 5, "Octobre": 0, "Novembre": 3, "Décembre": 5},
              "JOURS_SEMAINE": ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
              }


def jour_semaine(date_jour: str) -> str:
    """
    Cette fonction permet de trouver le jour de la semaine à l'aide d'une date.
    :param date_jour: la date pour laquelle on recherche le jour de la semaine.
    :return: le jour de la semaine correspondant à la date fournie en paramètre.
    """
    # On découpe la chaîne de caractères afin de récupérer le jour, le mois et l'année de la date
    date_jour = date_jour.split("/")
    num_jour, num_mois, num_annee = int(date_jour[0]), int(date_jour[1]), int(date_jour[2])

    valeur = num_annee % 100 + (num_annee % 100 // 4) + num_jour + CONSTANTES["SIECLES"][num_annee // 100]

    # On stocke le nom du mois correspondant à la date
    mois = list(CONSTANTES["VALEURS_MOIS"].keys())[num_mois - 1]

    # On ajoute la valeur correspondante au nom du mois
    valeur += CONSTANTES["VALEURS_MOIS"][mois]

    # Vérification Année Bissextile et janvier/février
    if (num_annee % 4 == 0 and num_annee % 100 != 0 or num_annee % 400 == 0) and (num_mois == 1 or num_mois == 2):
        valeur -= 1

    return CONSTANTES["JOURS_SEMAINE"][valeur % 7]


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    date = input("Donnez moi une date (au format JJ/MM/AAAA): ")
    print("Le %s est un %s" % (date, jour_semaine(date)))
