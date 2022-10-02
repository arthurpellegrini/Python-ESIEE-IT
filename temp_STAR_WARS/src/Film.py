#!/usr/bin/python
# -*- coding: utf-8 -*-

class Film:
    """
    Cette classe permet de définir un film de la saga Star Wars.
    """

    def __init__(self, titre: str, annee_sortie: int, num_episode: int, cout: float, recette: float):
        """
        Le constructeur de la classe Film.
        :param titre: Le titre du film.
        :param annee_sortie: L'année de sortie du film.
        :param num_episode: Le numéro de l'épisode de la sage Star Wars.
        :param cout: Le coût du tournage et de la diffusion film.
        :param recette: La recette du film.
        """
        self._titre = titre
        self._annee_sortie = annee_sortie
        self._num_episode = num_episode
        self._cout = cout
        self._recette = recette

    def get_titre(self):
        """

        """
        return self._titre

    def set_titre(self, titre):
        """
        
        """
        self._titre = titre

    def get_annee_sortie(self):
        return self._annee_sortie

    def set_annee_sortie(self, annee_sortie):
        self._annee_sortie = annee_sortie

    def get_num_episode(self):
        return self._num_episode

    def set_episode(self, num_episode):
        self._num_episode = num_episode

    def get_cout(self):
        return self._cout

    def set_cout(self, cout):
        self._cout = cout

    def get_recette(self):
        return self._recette

    def set_recette(self, recette):
        self._recette = recette

    def __str__(self, ):
        pass
