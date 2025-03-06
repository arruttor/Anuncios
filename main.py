from flask import Flask, redirect, render_template, request, flash, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Chave secreta necessária para flash messages

# Configuração da pasta de Upload
UPLOAD_FOLDER = os.path.join(basedir, 'static/anuncios')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo do Banco de Dados
class Anuncio(db.Model):
    __tablename__ = 'anuncios'
    id = db.Column(db.Integer, primary_key=True)
    caminho = db.Column(db.String(64))
    altura = db.Column(db.Integer)
    largura = db.Column(db.Integer)

    def __init__(self, caminho, altura, largura):
        self.caminho = caminho
        self.altura = altura
        self.largura = largura

    @staticmethod
    def criar_anuncio(caminho_arquivo, altura, largura):
        novo_anuncio = Anuncio(caminho=caminho_arquivo, altura=altura, largura=largura)
        db.session.add(novo_anuncio)
        db.session.commit()
        return novo_anuncio

    @staticmethod
    def deletar_todos():
        Anuncio.query.delete()
        db.session.commit()

    @staticmethod
    def get_all():
        return Anuncio.query.first()

# Verifica se a tabela do banco de dados já está criada
def verifica_tabela_criada():
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table(Anuncio.__tablename__):
            db.create_all()
            print('Tabela criada')
        else:
            print('Tabela já criada, sem alteração')

verifica_tabela_criada()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("Nenhum arquivo enviado!", "error")
            return redirect(url_for('home'))
        
        arquivo = request.files['file']
        largura = request.form['largura']
        altura = request.form['altura']
        if arquivo.filename == '':
            flash("Nenhum arquivo selecionado!", "error")
            return redirect(url_for('home'))
        
        nome_arquivo = arquivo.filename.replace(' ', '_')
        caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
        arquivo.save(caminho_arquivo)
       
        Anuncio.deletar_todos()
        anuncio = Anuncio.criar_anuncio(nome_arquivo, altura, largura)

        print(f'Anúncio criado com sucesso: {anuncio.caminho}, altura: {anuncio.altura}, largura: {anuncio.largura}')
        
        flash("Arquivo enviado com sucesso!", "success")
        return redirect(url_for('home'))
        
    return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('index.html')

@app.route('/anuncio')
def anuncio():
    data = Anuncio.get_all()
    if data:
        anuncios = os.path.join('static/anuncios', data.caminho)
        print(f'Anúncio recuperado: {data.caminho}, altura: {data.altura}, largura: {data.largura}')
        return render_template('fronty.html', anuncios=anuncios, altura=data.altura, largura=data.largura)
    else:
        print('Nenhum anúncio encontrado.')
        return render_template('fronty.html', anuncios=None)

@app.route('/teste')
def teste():
    return redirect("/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)