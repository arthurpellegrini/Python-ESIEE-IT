#!/usr/bin/python
# -*- coding: utf-8 -*-

# ============================================ DATA REFERENCE ============================================ #
# Saga : https://fr.wikipedia.org/wiki/Star_Wars_au_cin%C3%A9ma                                            #
# Coût + Recettes : http://www.cine-directors.net/starwars.htm                                             #
# Personnages : https://fr.wikipedia.org/wiki/Liste_des_personnages_encyclop%C3%A9diques_de_Star_Wars      #
# ======================================================================================================== #
from src import Film, Acteur, Personnage, Gentil, Mechant


def input_film() -> Film:
    """
    Cette fonction permet de récupérer les entrées nécessaires à la création d'un objet film.
    :return: L'objet Film correspondant aux entrées fournies par l'utilisateur.
    """
    titre = input("Entrer le nom du film : ")
    annee_sortie = int(input("Entrer l'année de sortie de l'épisode : "))
    num_episode = int(input("Entrer le numéro de l'épisode : "))
    cout = float(input("Entrer le cout du film (en million de $) : "))
    recette = float(input("Entrer les recettes du film (en million $) : "))
    return Film(titre, annee_sortie, num_episode, cout, recette)


def make_back_up(dictionnaire_films):
    """
    Cette fonction permet de d'afficher pour chaque film contenu dans le dictionnaire : son année, son titre et son
    bénéfice.
    :param dictionnaire_films:
    :return: Une chaîne de caractère structurée de la sorte : année - titre - bénéfice
    """
    for key in list(dictionnaire_films.keys()):
        film = dictionnaire_films.get(key)
        print(key, "-", film.get_titre(), "-", film.calcul_benefice()[0])


def print_collection(collection):
    """
    Cette fonction permet l'affichage des objets d'une collection.
    :param collection: Une collection qui peut être de n'importe quel type.
    :return:
    """
    if type(collection) is set or tuple:
        for obj in collection:
            print(obj)
    elif type(collection) is dict or map:
        for key in list(collection.keys):
            print(collection.get(key))
    elif type(collection) is list:
        for i in range(len(collection)):
            print(i, collection[i])
    else:
        print("/!\ Impossible d'afficher cette collection.")


if __name__ == "__main__":
    # Création de personnages
    personnage1 = Gentil("Solo", "Han")
    personnage2 = Gentil("Anakin", "Skywalker", True)
    personnage3 = Mechant("Dark", "Vador", True)
    personnage4 = Mechant("Leia", "Organa")

    # Création d'acteurs qui ont chacun un tuple de personnage
    acteur1 = Acteur("Harrison", "Ford", (personnage1, Personnage("Indiana", "Jones")))
    acteur2 = Acteur("Jake", "Lloyd", (personnage2, personnage3, Personnage("Jamie", "Langston")))
    acteur3 = Acteur("Vivien", "Lyra Blair", (personnage4, Personnage("Emily", "Gladstone")))

    # Les acteurs ne sont pas mis dans le même ordre dans les collections afin de tester le tri
    liste_acteurs1 = [acteur2, acteur1, acteur3]
    liste_acteurs2 = [acteur3, acteur1, acteur2]

    # Création d'objets Film
    film1 = Film("Un nouvel Espoir", 1977, 4, 11.0, 775.4, liste_acteurs1)
    film2 = Film("L'empire contre-attaque", 1980, 5, 18.0, 538.4, liste_acteurs2)
    # film3 = input_film()

    # Collection qui contient des objets Film
    liste_films = [film1, film2]  # , film3

    # Test fonction tri des acteurs
    film1.sort_acteurs()
    film2.sort_acteurs()

    # Affichage des objets de la collection
    print_collection(liste_films)

    # Test fonction make_back_up
    dictionnaire_films = {film1.get_annee_sortie(): film1, film2.get_annee_sortie(): film2}
    make_back_up(dictionnaire_films)

