#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import Personnage


class Mechant(Personnage):
    """
    Cette classe permet de définir un méchant de la saga Star Wars.
    """
    def __init__(self, nom: str, prenom: str, is_cote_obscur: bool = False):
        """
        Le constructeur de la classe Mechant.
        :param nom: Le nom de famille du méchant.
        :param prenom: Le prénom du méchant.
        :param is_cote_obscur: (par défaut False) True si le méchant est du côté obscur et False sinon.
        """
        super().__init__(nom, prenom)
        self._is_cote_obscur: bool = is_cote_obscur

    def get_is_cote_obscur(self) -> bool:
        """
        Accesseur de l'attribut _is_cote_obscur de la classe Mechant.
        :return: Un booléen correspondant au fait que le méchant soit du côté obscur ou non.
        """
        return self._is_cote_obscur

    def set_cote_obscur(self, is_cote_obscur: bool):
        """
        Mutateur de l'attribut _is_cote_obscur de la classe Mechant.
        :param is_cote_obscur: Le nouveau booléen correspondant au fait que le méchant soit du côté obscur ou non.
        """
        self._is_cote_obscur = is_cote_obscur

    def __str__(self):
        """
        Cette méthode permet de modifier le contenu de l'objet lors de sa conversion en str.
        :return: Une chaîne de caractères contenant tous les attributs de l'objet.
        """
        is_cote_obscur = "Côté Obscur" if self._is_cote_obscur else "Lambda"
        return super().__str__() + " -> " + is_cote_obscur
