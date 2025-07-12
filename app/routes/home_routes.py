import os
from flask import Blueprint, flash, render_template, request, redirect, url_for, current_app
from ..services.extensions import socketio

from ..models.Anuncio import Anuncio
from ..models.Mensagem import Mensagem
from ..models.Config import Config

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("Nenhum arquivo enviado!", "error")
            return redirect(url_for('home.home'))
        
        arquivos = request.files.getlist('file')
        mensagem = request.form['mensagem']
        local = request.form['local']
        Mensagem.deletar_todos()
        anuncio = []
        if arquivos and not all(arquivo.filename == '' for arquivo in arquivos):
            for arquivo in arquivos:
                nome_arquivo = arquivo.filename.replace(' ', '_')
                caminho_arquivo = os.path.join(current_app.config['UPLOAD_FOLDER'], nome_arquivo)
                arquivo.save(caminho_arquivo)
                anuncio.append(Anuncio.criar_anuncio(nome_arquivo,tamanho=os.path.getsize(caminho_arquivo), nome=nome_arquivo)) 

        mensagem = Mensagem.criar_mensagem(mensagem)
        local_atual = Config.get_configuracao()
        if local_atual:
            if local_atual != local:
                Config.atualizar_configuracao(local)
        else:
            Config.criar_configuracao(local)
        
        flash("Arquivo enviado com sucesso!", "success")
        socketio.emit('atualizar_anuncios')
        return redirect(url_for('cad.cadastro'))
        
    return render_template('home.html')

@home_bp.route('/cadastro/delete', methods=['POST'])
def delete():
    ids = request.form.getlist('selecionados')
    if not ids:
        flash("Nenhum arquivo selecionado para deletar.", "error")
        return redirect(url_for('cad.cadastro'))
    for id in ids:
        anuncio = Anuncio.query.get(id)
        if anuncio:
            caminho_arquivo = os.path.join(current_app.config['UPLOAD_FOLDER'], anuncio.caminho)
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)
            Anuncio.delete_select(anuncio)
    flash("Arquivos deletados com sucesso!", "success")
    socketio.emit('atualizar_anuncios')
    return redirect(url_for('cad.cadastro'))
