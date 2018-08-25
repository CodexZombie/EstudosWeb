# -*- coding: UTF-8 -*-
# python/models.py

#CADASTRO perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')

class Perfil(object):
    'Classe padrão para perfis de usuários'
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print 'Nome: %s' % (self.nome)
        print 'Telefone: %s' % (self.telefone)
        print 'Empresa: %s' % (self.empresa)
        print 'Curtidas: %s' % (self.__curtidas)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    @staticmethod
    def gerar_perfis(nome_arquivo):
        perfis = []
        arquivo = open(nome_arquivo, 'r')
        for linha in arquivo:
            valores = linha.split(',')
            perfis.append(Perfil(*valores))
        arquivo.close()
        return perfis



class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários VIPs'
    def __init__(self, nome, telefone, empresa, apelido):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0



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