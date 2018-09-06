# EStudo: Orientacao a Objetos
# ../python3/oo/teste.py

def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    saldo = conta['saldo']
    print('Saldo {}'.format(conta['saldo']))

