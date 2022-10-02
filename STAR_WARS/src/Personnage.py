#!/usr/bin/python
# -*- coding: utf-8 -*-

class Personnage:
    """
    Cette classe permet de définir un personnage de la saga Star Wars.
    """
    def __init__(self, nom: str, prenom: str):
        """
        Le constructeur de la classe Personnage.
        :param nom: Le nom de famille du personnage.
        :param prenom: Le prenom du personnage.
        """
        self._nom = nom
        self._prenom = prenom

    def get_nom(self) -> str:
        """
        Accesseur de l'attribut _nom de la classe Personnage.
        :return: Le nom de famille du personnage.
        """
        return self._nom

    def set_nom(self, nom: str):
        """
        Mutateur de l'attribut _nom de la classe Personnage.
        :param nom: Le nouveau nom de famille du personnage.
        """
        self._nom = nom

    def get_prenom(self) -> str:
        """
        Accesseur de l'attribut _prenom de la classe Personnage.
        :return: Le prenom du personnage.
        """
        return self._prenom

    def set_prenom(self, prenom: str):
        """
        Mutateur de l'attribut _prenom de la classe Personnage.
        :param prenom: Le nouveau prenom du personnage.
        """
        self._prenom = prenom

    def __str__(self):
        """
        Cette méthode permet de modifier le contenu de l'objet lors de sa conversion en str.
        :return: Une chaîne de caractères contenant tous les attributs de l'objet.
        """
        return "\n\t\t<PERSONNAGE ( Nom -> %s; Prénom -> %s)>" % (self._nom, self._prenom)

    def __repr__(self) -> str:
        """
        Cette méthode permet de représenter l'objet sous forme d'une chaîne de caractères.
        :return: Une chaîne de caractères correspondante à l'objet.
        """
        return "(%s; %s)" % (self._nom, self._prenom)
