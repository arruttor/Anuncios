from ..db import db
from datetime import datetime
import pytz

class Anuncio(db.Model):
    __tablename__ = 'anuncios'
    id = db.Column(db.Integer, primary_key=True)
    caminho = db.Column(db.String(64))
    altura = db.Column(db.Integer, default=0)
    largura = db.Column(db.Integer, default=0)
    tamanho = db.Column(db.Integer, default=0)
    nome = db.Column(db.String(64), default='Anúncio')
    data_criacao = db.Column(db.DateTime)

    def __init__(self, caminho,tamanho, nome):
        self.caminho = caminho
        self.tamanho = tamanho
        self.nome = nome
        self.data_criacao = datetime.now(pytz.timezone('America/Sao_Paulo'))

    @staticmethod
    def criar_anuncio(caminho_arquivo, tamanho, nome):
        tamanho = tamanho / (1024 * 1024)
        tamanho = round(tamanho, 2)
        novo_anuncio = Anuncio(caminho=caminho_arquivo, tamanho=tamanho, nome=nome)
        db.session.add(novo_anuncio)
        db.session.commit()
        return novo_anuncio

    @staticmethod
    def deletar_todos():
        Anuncio.query.delete()
        db.session.commit()

    @staticmethod
    def get_all():
        return Anuncio.query.all()
    
    @staticmethod
    def delete_select(anuncio):
        if anuncio:
            db.session.delete(anuncio)
        db.session.commit()