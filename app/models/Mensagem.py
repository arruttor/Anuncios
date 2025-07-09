from ..db import db



class Mensagem(db.Model):
    __tablename__ = 'mensagens'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False)

    def __init__(self, texto):
        self.texto = texto
    
    @staticmethod
    def criar_mensagem(texto):
        nova_mensagem = Mensagem(texto=texto)
        db.session.add(nova_mensagem)
        db.session.commit()
        return nova_mensagem

    @staticmethod
    def deletar_todos():
        Mensagem.query.delete()
        db.session.commit()

    @staticmethod
    def get_all():
        return Mensagem.query.all()



    def __repr__(self):
        return f'<Mensagem {self.texto}>'   