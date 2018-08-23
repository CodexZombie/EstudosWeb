# -*- coding: UTF-8 -*-
# python/app.py

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    nome = raw_input()

    if((nome in nomes) == True):
        print 'Digite o novo nome:'
        novo_nome = raw_input()
        posicao = nomes.index(nome)
        nomes[posicao] = novo_nome

    if((nome in nomes) == False):
        print 'O nome digitado nao esta na lista.'

def procurar_regex(nomes):
    import re
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print (resultados)

def menu():
    nomes = []
    escolha = ''

    while(escolha != '0'):
        print 'Opções: 1 Cadastrar, 2 Listar, 3 Remover, 4 Alterar, 5 Procurar Regex, 0 para encerrar.'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)
        
        if(escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

        if (escolha == '4'):
            alterar(nomes)

        if (escolha == '5'):
            procurar_regex(nomes)

menu()