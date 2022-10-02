#!/usr/bin/python
# -*- coding: utf-8 -*-

from Personnage import Personnage


class Mechant(Personnage):
    def __init__(self):
        super().__init__()
        self._cote_obscur: bool = False

    def get_cote_obscur(self):
        return self._cote_obscur

    def set_cote_obscur(self, cote_obscur):
        self._cote_obscur = cote_obscur

    def __str__(self, ):
        pass
