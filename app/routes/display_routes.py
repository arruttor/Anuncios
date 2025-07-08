import os
from flask import Blueprint, flash, render_template, request, session, redirect, url_for
import socketio
import app
from ..models.Anuncio import Anuncio

disp_bp = Blueprint('disp', __name__)






@disp_bp.route('/anuncio')
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