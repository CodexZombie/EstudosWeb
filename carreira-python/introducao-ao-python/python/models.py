# -*- coding: UTF-8 -*-
# python/models.py

class Perfil(object):
    'Classe padrão para perfis de usuários'
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprime(self):
        print 'Nome: %s' % (self.nome)
        print 'Telefone: %s' % (self.telefone)
        print 'Empresa: %s' % (self.empresa)

class Data(object):
    def __init__ (self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print '%s/%s/%s' % (str(self.dia), str(self.mes), str(self.ano))

class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprime(self):
        imc = self.peso / (self.altura*self.altura)
        print 'IMC de %s: %s' % (self.nome, str(imc))