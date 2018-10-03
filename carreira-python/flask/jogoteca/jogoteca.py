from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self.__nome = nome
        self.__categoria = categoria
        self.__plataforma = plataforma

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def plataforma(self):
        return self.__plataforma


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Super Mario', 'Aventura', 'Super Nintendo')
jogo3 = Jogo('Pokemon Silver', 'RPG', 'Game Boy')

lista = [jogo1, jogo2, jogo3]


@app.route('/inicio')
def ola():
    return render_template('lista.html',
                           titulo='Jogos',
                           jogos=lista)


app.run()
