# -*- coding: UTF-8 -*-
#Builder Pattern
#../design-patterns-python/criador_de_nota_fiscal.py

from nota_fiscal import Nota_fiscal, Item

class criador_de_nota_fiscal(object):

    def __init__(self):

        self.__razao_social = None
        self.__cnpj = None
        self.__itens = None
        self.__data_de_emissao = None
        self.__detalhes = ''

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self
    
    
    def constroi(self):
        if(self.__razao_social is None):
            raise NameError('O campo Razao Social deve ser preenchido.')

        if(self.__cnpj is None):
            raise NameError('O campo CNPJ deve ser preenchido.')

        if(self.__itens is None):
            raise NameError('Ao menos um Item precisa constar na nota.')

        return Nota_fiscal(
            razao_social = self.__razao_social,
            cnpj = self.__cnpj,
            itens = self.__itens,
            data_de_emissao = self.__data_de_emissao,
            detalhes = self.__detalhes
        )
