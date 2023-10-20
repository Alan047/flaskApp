from flask import Flask, render_template

app = Flask(__name__)



#ROTAS 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fora')
def fora():
    return 'flaskApp'

