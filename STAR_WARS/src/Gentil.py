#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import Personnage


class Gentil(Personnage):
    """
    Cette classe permet de définir un gentil de la saga Star Wars.
    """
    def __init__(self, nom: str, prenom: str, is_force: bool = False):
        """
        Le constructeur de la classe Gentil.
        :param nom: Le nom de famille du gentil.
        :param prenom: Le prénom du gentil.
        :param is_force: (par défaut False) True si le gentil est de la force et False sinon.
        """
        super().__init__(nom, prenom)
        self._is_force: bool = is_force

    def get_is_force(self) -> bool:
        """
        Accesseur de l'attribut _is_force de la classe Gentil.
        :return: Un booléen correspondant au fait que le gentil soit de la force ou non.
        """
        return self._is_force

    def set_is_force(self, is_force: bool):
        """
        Mutateur de l'attribut _is_force de la classe Gentil.
        :param is_force: Le nouveau booléen correspondant au fait que le gentil soit de la force ou non.
        """
        self._is_force = is_force

    def __str__(self):
        """
        Cette méthode permet de modifier le contenu de l'objet lors de sa conversion en str.
        :return: Une chaîne de caractères contenant tous les attributs de l'objet.
        """
        is_force = "Force" if self._is_force else "Lambda"
        return super().__str__() + " -> " + is_force
