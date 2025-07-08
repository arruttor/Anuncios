from flask import Blueprint, render_template
cad_bp = Blueprint('cad', __name__)



@cad_bp.route('/cadastro')
def cadastro():
    return render_template('index.html')