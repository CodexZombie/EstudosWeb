# -*- coding: UTF-8 -*-

#../design-patterns-python/calculador_de_descontos.py

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        ).calcula(orcamento)
         
        return desconto


if __name__ == '__main__':

    from orcamento import Orcamento, Item
    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item 1', 100.0))
    orcamento.adiciona_item(Item('Item 2', 100.0))
    orcamento.adiciona_item(Item('Item 3', 100.0))
    orcamento.adiciona_item(Item('Item 4', 700.0))
    #orcamento.adiciona_item(Item('Item 5', 100.0))
    #orcamento.adiciona_item(Item('Item 6', 100.0))


    calculo = Calculador_de_descontos()
    desconto = calculo.calcula(orcamento)

    print 'Desconto Calculado: R$%s' % (desconto)
