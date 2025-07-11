from ..db import db

class Anuncio(db.Model):
    __tablename__ = 'anuncios'
    id = db.Column(db.Integer, primary_key=True)
    caminho = db.Column(db.String(64))
    altura = db.Column(db.Integer)
    largura = db.Column(db.Integer)
    tamanho = db.Column(db.Integer, default=0)
    nome = db.Column(db.String(64), default='Anúncio')
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, caminho, altura, largura,tamanho, nome):
        self.caminho = caminho
        self.altura = altura
        self.largura = largura
        self.tamanho = tamanho
        self.nome = nome
        self.data_criacao = db.func.current_timestamp()

    @staticmethod
    def criar_anuncio(caminho_arquivo, altura, largura, tamanho, nome):
        tamanho = tamanho / (1024 * 1024)
        tamanho = round(tamanho, 2)
        novo_anuncio = Anuncio(caminho=caminho_arquivo, altura=altura, largura=largura, tamanho=tamanho, nome=nome)
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