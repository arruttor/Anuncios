import os
from flask import Blueprint, flash, render_template, request, session, redirect, url_for
import socketio
import app
from ..models.Anuncio import Anuncio
from ..models.Mensagem import Mensagem

disp_bp = Blueprint('disp', __name__)






@disp_bp.route('/anuncio')
def anuncio():
    data = Anuncio.get_all()
    msg = Mensagem.get_all()
    anuncios = []
    if data:
        for anuncio in data:
            anuncios.append(os.path.join('static/anuncios', anuncio.caminho))
        
    if msg:    
        mensagem = msg[0].texto    
        return render_template('fronty.html', anuncios=anuncios, mensagem=mensagem)
    else:
        print('Nenhum anúncio encontrado.')
        return render_template('fronty.html', anuncios=None)