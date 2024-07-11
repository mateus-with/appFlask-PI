import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from config import db

app = Flask(__name__)

from controllers.controller import register_routes

register_routes(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/relos')
def relos():
    return render_template('relos.html')

HOST = 'localhost'
PORT = 4000
DEBUG = True

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
