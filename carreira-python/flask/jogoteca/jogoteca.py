from flask import Flask, render_template, request, redirect

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


@app.route('/')
def index():
    return render_template('lista.html',
                           titulo='Jogos',
                           jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html',
                           titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    plataforma = request. form['console']

    jogo = Jogo(nome, categoria, plataforma)
    lista.append(jogo)

    return redirect('/')


app.run(debug=True)
