# -*- coding: UTF-8 -*-
# Design Pattern Observer
#../design-patterns-python/observer.py

def envia_por_email(nota_fiscal):
    print 'Enviando nota por email %s...' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
    print 'Salvando a nota %s...' % (nota_fiscal.cnpj)

def imprime(nota_fiscal):
    print 'Imprimindo a nota %s...' % (nota_fiscal.cnpj)