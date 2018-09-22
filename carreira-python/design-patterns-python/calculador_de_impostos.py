# -*- coding: UTF-8 -*-
#../design-patterns-python/calculador_de_impostos.py

class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print valor


if __name__ == '__main__':

    from orcamento import Orcamento, Item
    from impostos import ICMS, ISS, IKCV, ICPP

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item 1', 20))
    orcamento.adiciona_item(Item('Item 2', 20))
    orcamento.adiciona_item(Item('Item 3', 20))
    orcamento.adiciona_item(Item('Item 4', 20))
    orcamento.adiciona_item(Item('Item 5', 200))

    calculador_de_impostos = Calculador_de_impostos()
    
    print 'ICMS R$'
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
    print 'ISS R$'
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    print 'ICPP R$'
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    print 'IKCV R$'
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())

