#!/usr/bin/python
# -*- coding: utf-8 -*-

class Acteur:
    """
    Cette classe permet de définir un acteur.
    """
    def __init__(self, nom: str, prenom: str, personnages: tuple = tuple()):
        """
        Le constructeur de la classe Acteur.
        :param nom: Le nom de famille de l'acteur.
        :param prenom: Le prenom de l'acteur.
        :param personnages: Les personnages qui ont été joués par l'acteur.
        """
        self._nom = nom
        self._prenom = prenom
        self._personnages = personnages

    def get_nom(self) -> str:
        """
        Accesseur de l'attribut _nom de la classe Acteur.
        :return: Le nom de famille de l'acteur.
        """
        return self._nom

    def set_nom(self, nom: str):
        """
        Mutateur de l'attribut _nom de la classe Acteur.
        :param nom: Le nouveau nom de famille de l'acteur.
        """
        self._nom = nom

    def get_prenom(self) -> str:
        """
        Accesseur de l'attribut _prenom de la classe Acteur.
        :return: Le prenom de l'acteur.
        """
        return self._prenom

    def set_prenom(self, prenom: str):
        """
        Mutateur de l'attribut _prenom de la classe Acteur.
        :param prenom: Le nouveau prenom de l'acteur.
        """
        self._prenom = prenom

    def get_personnages(self) -> tuple:
        """
        Accesseur de l'attribut _personnages de la classe Acteur.
        :return: Les personnages de film qui ont été joué par l'acteur.
        """
        return self._personnages

    def set_personnages(self, personnages: tuple):
        """
        Mutateur de l'attribut _personnages de la classe Acteur.
        :param personnages: Le nouveau tuple contenant les personnages de film joués par l'acteur.
        """
        self._personnages = personnages

    def nb_personnages(self) -> int:
        """
        Cette méthode permet de connaître le nombre de personnages joués par l'acteur.
        :return: Le nombre de personnages joués par l'acteur.
        """
        return len(self._personnages)

    def __str__(self):
        """
        Cette méthode permet de modifier le contenu de l'objet lors de sa conversion en str.
        :return: Une chaîne de caractères contenant tous les attributs de l'objet.
        """
        return "\n\t<ACTEUR [ Nom -> %s; Prénom -> %s; Personnages -> %s ]>" % \
               (self._nom, self._prenom, ", ".join([str(personnage) for personnage in self._personnages]))

    def __repr__(self) -> str:
        """
        Cette méthode permet de représenter l'objet sous forme d'une chaîne de caractères.
        :return: Une chaîne de caractères correspondante à l'objet.
        """
        return "(%s; %s; %s)" % (self._nom, self._prenom, self._personnages)
