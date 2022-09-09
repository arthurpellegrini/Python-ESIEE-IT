CONSTANTES = {"SIECLES": {16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4},
              "VALEURS_MOIS": {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5},
              "JOURS_SEMAINE": ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
              }


def jour_semaine(date_jour: str) -> str:
    """
    Cette fonction permet de trouver le jour de la semaine à l'aide d'une date.
    :param date_jour: la date pour laquelle on recherche le jour de la semaine.
    :return: le jour de la semaine correspondant à la date fournie en paramètre.
    """
    date_jour = date_jour.split("/")
    num_jour, mois, annee = int(date_jour[0]), int(date_jour[1]), int(date_jour[2])

    jour = annee % 100 + (annee % 100 // 4) + num_jour
    jour += CONSTANTES["VALEURS_MOIS"][mois] + CONSTANTES["SIECLES"][annee // 100]

    # Vérification Année Bissextile et janvier/février
    if (annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0) and (mois == 1 or mois == 2):
        jour -= 1

    return CONSTANTES["JOURS_SEMAINE"][jour % 7]


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    date = input("Donnez moi une date (au format JJ/MM/AAAA): ")
    print("Le %s est un %s" % (date, jour_semaine(date)))
