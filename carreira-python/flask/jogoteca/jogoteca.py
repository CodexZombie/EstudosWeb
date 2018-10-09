from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'jogoteca'

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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')


app.run(debug=True)
