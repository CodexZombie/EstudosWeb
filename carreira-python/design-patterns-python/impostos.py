# -*- coding: UTF-8 -*-
#../design-patterns-python/impostos.py

class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
    