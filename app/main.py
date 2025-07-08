from flask import Flask, redirect, render_template, request, flash, url_for
from db import db
from models.Anuncio import Anuncio
import os
from services.base_services import verifica_tabela_criada
import config
from flask_socketio import SocketIO
import gevent
import gevent.monkey


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


gevent.monkey.patch_all()

socketio = SocketIO(app, async_mode='gevent')


# Verifica se a tabela do banco de dados já está criada
verifica_tabela_criada()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("Nenhum arquivo enviado!", "error")
            return redirect(url_for('home'))
        
        arquivos = request.files.getlist('file')
        largura = request.form['largura']
        altura = request.form['altura']
        # if arquivo.filename == '':
        #     flash("Nenhum arquivo selecionado!", "error")
        #     return redirect(url_for('home'))
       
        Anuncio.deletar_todos()
        anuncio = []
        for arquivo in arquivos:
            nome_arquivo = arquivo.filename.replace(' ', '_')
            caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
            arquivo.save(caminho_arquivo)
            anuncio.append(Anuncio.criar_anuncio(nome_arquivo, altura, largura)) 

        
        flash("Arquivo enviado com sucesso!", "success")
        socketio.emit('atualizar_anuncios')
        return redirect(url_for('home'))
        
    return render_template('home.html')

@app.route('/cadastro')
def cadastro():
    return render_template('index.html')

@app.route('/anuncio')
def anuncio():
    data = Anuncio.get_all()
    anuncios = []
    if data:
        for anuncio in data:
            anuncios.append(os.path.join('static/anuncios', anuncio.caminho))

        return render_template('fronty.html', anuncios=anuncios)
    else:
        print('Nenhum anúncio encontrado.')
        return render_template('teste.html', anuncios=None)


if __name__ == '__main__':
   app.run( debug=False, host='0.0.0.0', port=5000)