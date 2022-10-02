#!/usr/bin/python
# -*- coding: utf-8 -*-

class Personnage:
    """
    Cette classe permet de définir un personnage de la saga Star Wars.
    """
    def __init__(self):
        """
        Le constructeur de la classe Personnage.
        """
        self._nom = None
        self._prenom = None

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_prenom(self):
        return self._prenom

    def set_prenom(self, prenom):
        self._prenom = prenom

    def __str__(self, ):
        pass
