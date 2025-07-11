import os
from flask import Blueprint, flash, render_template, request, redirect, url_for, current_app
from ..services.extensions import socketio

from ..models.Anuncio import Anuncio
from ..models.Mensagem import Mensagem

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("Nenhum arquivo enviado!", "error")
            return redirect(url_for('home.home'))
        
        arquivos = request.files.getlist('file')
        largura = request.form['largura']
        altura = request.form['altura']
        mensagem = request.form['mensagem']
        # if arquivo.filename == '':
        #     flash("Nenhum arquivo selecionado!", "error")
        #     return redirect(url_for('home'))
    
        Anuncio.deletar_todos()
        Mensagem.deletar_todos()
        anuncio = []
        for arquivo in arquivos:
            nome_arquivo = arquivo.filename.replace(' ', '_')
            caminho_arquivo = os.path.join(current_app.config['UPLOAD_FOLDER'], nome_arquivo)
            arquivo.save(caminho_arquivo)
            anuncio.append(Anuncio.criar_anuncio(nome_arquivo, altura, largura,tamanho=os.path.getsize(caminho_arquivo))) 

        mensagem = Mensagem.criar_mensagem(mensagem)    

        
        flash("Arquivo enviado com sucesso!", "success")
        socketio.emit('atualizar_anuncios')
        return redirect(url_for('home.home'))
        
    return render_template('home.html')
