# -*- coding: UTF-8 -*-
# DSL e Interpreter
#../design-patterns-python/contrato.py

from abc import abstractmethod, ABCMeta

class Expressao(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def avalia(self): pass


class Subtracao(Expressao):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia())


class Soma(Expressao):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia())


class Numero(Expressao):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == '__main__':

    expressao_esquerda = Subtracao(Numero(100), Numero(50))
    print expressao_esquerda.avalia()

    expressao_direita = Soma(Numero(20), Numero(30))
    print expressao_direita.avalia()

    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    print expressao_conta.avalia()