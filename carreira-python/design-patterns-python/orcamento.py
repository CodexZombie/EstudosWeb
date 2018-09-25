# -*- coding: UTF-8 -*-
#../design-patterns-python/orcamento.py

from abc import ABCMeta, abstractmethod


class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.desconto_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento): pass

    @abstractmethod
    def aprova(self, orcamento): pass

    @abstractmethod
    def reprova(self, orcamento): pass

    @abstractmethod
    def finaliza(self, orcamento): pass


class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        if (not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True
        else:
            raise Exception('O Desconto ja foi aplicado')

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orcamentos em aprovacao devem ser Aprovados ou Reprovados antes de serem finalizados')


class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        if (not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception('O Desconto ja foi aplicado')

    def aprova(self, orcamento):
        raise Exception('O orcamento ja esta aprovado.')
        
    def reprova(self, orcamento):
        raise Exception('Orcamentos Aprovados nao podem ser reprovados.')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()



class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos Reprovados nao recebem desconto extra.')

    def aprova(self, orcamento):
        raise Exception('Orcamentos Reprovados nao podem ser aprovados.')
        
    def reprova(self, orcamento):
        raise Exception('O orcamento ja foi reprovado.')

    def finaliza(self, orcamento):
        raise Exception('Orcamentos reprovados nao podem ser Finalizados.')


class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos Finalizados nao recebem desconto extra.')

    def aprova(self, orcamento):
        raise Exception('O orcamento ja esta Finalizado, nao pode ser aprovado.')
        
    def reprova(self, orcamento):
        raise Exception('O orcamento ja esta Finalizado, nao podem ser reprovados.')

    def finaliza(self, orcamento):
        raise Exception('O orcamento ja esta Finalizado.')



class Orcamento(object):
    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0.0

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aprova(self):
        self.estado_atual.aprova(self)
    
    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)


class Item(object):
    
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    orcamento.aplica_desconto_extra() 
    print orcamento.valor
    orcamento.aprova()

    orcamento.aplica_desconto_extra()
    print orcamento.valor
    orcamento.finaliza()

    orcamento.aplica_desconto_extra()
