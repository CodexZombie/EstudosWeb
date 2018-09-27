# -*- coding: UTF-8 -*-
# DSL e Interpreter
#../design-patterns-python/operacoes.py

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

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Soma(Expressao):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia())

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self, visitor):
        visitor.visita_soma(self)    



class Numero(Expressao):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


if __name__ == '__main__':

    from impressao import Impressao

    visitor = Impressao()
    
    expressao_esquerda = Subtracao(Numero(100), Numero(50))
    print 'Expressao esquerda = ',
    expressao_esquerda.aceita(visitor)
    print ''

    expressao_direita = Soma(Numero(20), Numero(30))
    print 'Expressao direita = ',
    expressao_direita.aceita(visitor)
    print ''

    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    print ''

    expressao_conta.aceita(visitor),
    print '= %s' % (expressao_conta.avalia())