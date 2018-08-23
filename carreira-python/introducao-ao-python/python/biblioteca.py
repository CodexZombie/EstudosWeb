# -*- coding: UTF-8 -*-
# python/biblioteca.py

def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial : posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(nome_convidado):
    print "Enviando convite para %s" % (nome_convidado)

def processa_convite(convidado):
    nome_formatado = gera_nome_convite(convidado)
    envia_convite(nome_formatado)

def idade(ano_como_string):
    ano_como_string = raw_input()
    ano_como_int = int(ano_como_string)
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_como_int
    return idade
