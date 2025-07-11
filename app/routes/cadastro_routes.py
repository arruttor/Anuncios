from flask import Blueprint, render_template
from ..models.Anuncio import Anuncio
import os
cad_bp = Blueprint('cad', __name__)



@cad_bp.route('/cadastro')
def cadastro():
    data = Anuncio.get_all()
    if data:
        return render_template('index.html', anuncios=data)
    else: 
        return render_template('index.html', anuncios=None)

    