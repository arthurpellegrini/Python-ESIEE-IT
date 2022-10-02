#!/usr/bin/python
# -*- coding: utf-8 -*-

class Film:
    """
    Cette classe permet de définir un film de la saga Star Wars.
    """

    def __init__(self, titre: str, annee_sortie: int, num_episode: int, cout: float, recette: float, acteurs=None):
        """
        Le constructeur de la classe Film.
        :param titre: Le titre du film.
        :param annee_sortie: L'année de sortie du film.
        :param num_episode: Le numéro de l'épisode de la sage Star Wars.
        :param cout: Les coûts liés à la production et à la diffusion du film (en million de $).
        :param recette: Les recettes générées par le film (en million de $).
        :param acteurs: Une collection contenant les acteurs du film.
        """
        self._titre = titre
        self._annee_sortie = annee_sortie
        self._num_episode = num_episode
        self._cout = cout
        self._recette = recette
        if acteurs is None:
            acteurs = list()
        self._acteurs = list(acteurs)

    def get_titre(self) -> str:
        """
        Accesseur de l'attribut _titre de la classe Film.
        :return: Le titre du film.
        """
        return self._titre

    def set_titre(self, titre: str):
        """
        Mutateur de l'attribut _titre de la classe Film.
        :param titre: Le nouveau titre du film.
        """
        self._titre = titre

    def get_annee_sortie(self) -> int:
        """
        Accesseur de l'attribut _annee_sortie de la classe Film.
        :return: L'année de sortie du film.
        """
        return self._annee_sortie

    def set_annee_sortie(self, annee_sortie: int):
        """
        Mutateur de l'attribut _annee_sortie de la classe Film.
        :param annee_sortie: La nouvelle année de sortie du film.
        """
        self._annee_sortie = annee_sortie

    def get_num_episode(self) -> int:
        """
        Accesseur de l'attribut _num_episode de la classe Film.
        :return: Le numéro correspondant à l'épisode du film.
        """
        return self._num_episode

    def set_episode(self, num_episode: int):
        """
        Mutateur de l'attribut _num_episode de la classe Film.
        :param num_episode: Le nouveau numéro correspondant à l'épisode du film.
        """
        self._num_episode = num_episode

    def get_cout(self) -> float:
        """
        Accesseur de l'attribut _cout de la classe Film.
        :return: Le coût de production et diffusion du film.
        """
        return self._cout

    def set_cout(self, cout: float):
        """
        Mutateur de l'attribut _cout de la classe Film.
        :param cout: Le nouveau total des coûts liés à la production et à la diffusion du film.
        """
        self._cout = cout

    def get_recette(self) -> float:
        """
        Accesseur de l'attribut _recette de la classe Film.
        :return: Le total des recettes générées par le film.
        """
        return self._recette

    def set_recette(self, recette: float):
        """
        Mutateur de l'attribut _recette de la classe Film.
        :param recette: Le nouveau total des recettes générées par le film.
        """
        self._recette = recette

    def get_acteurs(self) -> list:
        """
        Accesseur de l'attribut _acteurs de la classe Film.
        :return: La liste des acteurs ayant joué dans le film.
        """
        return self._acteurs

    def set_acteurs(self, acteurs: list):
        """
        Mutateur de l'attribut _acteurs de la classe Film.
        :param acteurs: La nouvelle liste des acteurs ayant joué dans le film.
        """
        self._acteurs = acteurs

    def nb_acteurs(self) -> int:
        """
        Cette méthode permet de connaître le nombre d'acteurs jouant dans le film.
        :return: Le nombre d'acteurs qui jouent dans le film.
        """
        return len(self._acteurs)

    def nb_personnages(self) -> int:
        """
        Cette méthode permet de connaître le nombre total de personnages dans le film.
        :return: Le nombre total de personnages dans le film (tous les personnages joués par tous les acteurs).
        """
        nb_personnages = 0
        for acteur in self._acteurs:
            nb_personnages += acteur.nb_personnages()
        return nb_personnages

    def sort_acteurs(self):
        """
        Cette méthode permet de trier les acteurs par ordre alphabétique des noms de familles puis des prénoms.
        """
        not_sort = True
        while not_sort:
            not_sort = False
            for i in range(len(self.get_acteurs())-1):
                if self.get_acteurs()[i].get_nom().lower()[:1] > self.get_acteurs()[i+1].get_nom().lower()[:1]:
                    temp = self.get_acteurs()[i]
                    self.get_acteurs()[i] = self.get_acteurs()[i+1]
                    self.get_acteurs()[i+1] = temp
                    not_sort = True

    def calcul_benefice(self) -> (float, bool):
        """
        Cette méthode permet de calculer les bénéfices (en Millions de $) à l'aide de son coût ainsi que de ces
        recettes.
        :return: Le bénéfice du film.
        """
        benefice = self._recette - self._cout
        return (benefice, True) if benefice >= 0 else (benefice, False)

    def is_before(self, annee_film: int) -> bool:
        """
        Cette méthode permet de savoir si le film est sortie avant un autre.
        :param annee_film: L'année du film à comparer.
        :return: True si l'année passée en paramètre est supérieure à l'année de l'objet et False si l'année passée
        en paramètre est antérieure à l'année de l'objet.
        """
        return True if self._annee_sortie < annee_film else False

    def __str__(self) -> str:
        """
        Cette méthode permet de modifier le contenu de l'objet lors de sa conversion en str.
        :return: Une chaîne de caractères contenant tous les attributs de l'objet.
        """
        return "\n<== FILM { Titre -> %s; Sortie -> %d; Épisode -> %d; Coût -> %0.3f M$; " \
               "Recette -> %0.3f M$; Acteurs -> %s } ==>\n" % \
               (self._titre, self._annee_sortie, self._num_episode, self._cout, self._recette,
                ", ".join([str(acteur) for acteur in self._acteurs]))

    def __repr__(self) -> str:
        """
        Cette méthode permet de représenter l'objet sous forme d'une chaîne de caractères.
        :return: Une chaîne de caractères correspondante à l'objet.
        """
        return "(%s; %d; %d; %0.3f; %0.3f; %s)" % (self._titre, self._annee_sortie, self._num_episode, self._cout,
                                                   self._recette, self._acteurs)
