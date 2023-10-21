from flask import Flask, render_template, request, redirect
from banco_dados import inserir, show_table, deletar

app = Flask(__name__)



#ROTAS 

@app.route('/')
def home():
    return render_template('index.html',dados=show_table())

@app.route('/fora')
def fora():
    return 'flaskApp'

@app.route('/processar', methods=['POST'])
def processar():
    nome = request.form.get('nome')
    post = request.form.get('texto-publicação')
    inserir(nome, post)
    return redirect('/')

@app.route('/administar_posts')
def administar_posts():
    return render_template('deletar.html', dados=show_table())

@app.route('/deletar', methods=['POST'])
def deletar_post():
    deletar(request.form.get('post-excluir'))
    
    

    return redirect('/administar_posts')


