from flask import Blueprint, render_template
from ..models.Anuncio import Anuncio
from ..models.Config import Config
import os
cad_bp = Blueprint('cad', __name__)



@cad_bp.route('/cadastro')
def cadastro():
    data = Anuncio.get_all()
    config = Config.get_configuracao()
    if config:
        local = config
    else:
        local = ""
    if data:

        return render_template('index.html', anuncios=data,local=local)
    else: 
        return render_template('index.html', anuncios=None, local=local)

    