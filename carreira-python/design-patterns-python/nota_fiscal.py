# -*- coding: UTF-8 -*-
#../design-patterns-python/nota_fiscal.py

from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        if (len(detalhes) > 20):
            raise Exception('Detalhes da nota fiscal não pode ter mais de 20 caracteres.')
        self.__detalhes = detalhes

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':

    from observadores import envia_por_email, salva_no_banco, imprime

    itens=[
        Item(descricao='Item A', valor=100),
        Item(descricao='Item B', valor=200)
    ]

    nota_fiscal = Nota_fiscal(
        cnpj='012345678901234',
        razao_social='FHSA Ltda',
        itens = itens,
        observadores=[envia_por_email, salva_no_banco, imprime]
    )
