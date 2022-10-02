#!/usr/bin/python
# -*- coding: utf-8 -*-

from Personnage import Personnage


class Gentil(Personnage):
    def __init__(self):
        super().__init__()
        self._force: bool = False

    def get_force(self):
        return self._force

    def set_force(self, force):
        self._force = force

    def __str__(self, ):
        pass
