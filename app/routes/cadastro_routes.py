from flask import Blueprint, render_template
from ..models.Anuncio import Anuncio
import os
cad_bp = Blueprint('cad', __name__)



@cad_bp.route('/cadastro')
def cadastro():
    data = Anuncio.get_all()
    if data:
        return render_template('teste.html', anuncios=data)

    