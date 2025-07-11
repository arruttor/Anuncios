from ..db import db

class Anuncio(db.Model):
    __tablename__ = 'anuncios'
    id = db.Column(db.Integer, primary_key=True)
    caminho = db.Column(db.String(64))
    altura = db.Column(db.Integer)
    largura = db.Column(db.Integer)
    tamanho = db.Column(db.Integer, default=0)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, caminho, altura, largura,tamanho):
        self.caminho = caminho
        self.altura = altura
        self.largura = largura
        self.tamanho = tamanho
        self.data_criacao = db.func.current_timestamp()

    @staticmethod
    def criar_anuncio(caminho_arquivo, altura, largura, tamanho):
        novo_anuncio = Anuncio(caminho=caminho_arquivo, altura=altura, largura=largura, tamanho=0)
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