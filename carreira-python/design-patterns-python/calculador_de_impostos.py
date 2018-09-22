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
    
    print 'ICMS seguido de ISS:'
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    
    print '\nICMS com ISS:'
    ISS_com_ICMS = ISS(ICMS())
    calculador_de_impostos.realiza_calculo(orcamento, ISS_com_ICMS)

    print '\nICPP seguido de IKCV:'
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())

    print '\nICPP com IKCV:'
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))

