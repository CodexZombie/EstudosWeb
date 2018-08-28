# Menu de seleção dos jogos

import forca
import adivinhacao


print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print('(1) Forca (2) Adivinhação')

jogo = int(input('Qual jogo? '))

if (jogo == 1):
    print('Jogando Forca.\n\n')
    forca.jogar()
elif (jogo == 2):
    print('Jogando Adivinhação.\n\n')
    adivinhacao.jogar()
