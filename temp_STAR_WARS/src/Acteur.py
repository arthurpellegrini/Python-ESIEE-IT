#!/usr/bin/python
# -*- coding: utf-8 -*-

class Acteur:
    """
    Cette classe permet de définir un acteur.
    """

    def __init__(self, nom: str, prenom: str):
        """
        Le constructeur de la classe Acteur.
        :param nom: Le nom de famille de l'acteur.
        :param prenom: Le prenom de l'acteur.
        """
        self._nom = nom
        self._prenom = prenom

    def get_nom(self) -> str:
        """
        Accesseur de l'attribut nom de la classe Acteur.
        :return str: Le nom de l'acteur.
        """
        return self._nom

    def set_nom(self, nom: str) -> None:
        """
        Mutateur de l'attribut nom de la classe Acteur.
        :param nom: Le nouveau nom de l'acteur.
        """
        self._nom = nom

    def get_prenom(self) -> str:
        return self._prenom

    def set_prenom(self, prenom: str) -> None:
        self._prenom = prenom

    def __str__(self, ):
        pass
