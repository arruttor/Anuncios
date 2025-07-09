from ..db import db



class Mensagem(db.Model):
    __tablename__ = 'mensagem'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False)

    def __init__(self, texto):
        self.texto = texto

    def __repr__(self):
        return f'<Mensagem {self.texto}>'   