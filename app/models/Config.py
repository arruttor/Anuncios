from ..db import db

class Config(db.Model):
    __tablename__ = 'configuracoes'
    id = db.Column(db.Integer, primary_key=True)
    local = db.Column(db.String(100), nullable=False)

    def __init__(self, local):
        self.local = local  
    
    @staticmethod
    def criar_configuracao(local):
        nova_configuracao = Config(local=local)
        db.session.add(nova_configuracao)
        db.session.commit()
        return nova_configuracao
    
    @staticmethod
    def get_configuracao():
        configuracao = Config.query.first()
        if configuracao:
            return configuracao.local
        return None
    
    @staticmethod
    def deletar_todos():
        Config.query.delete()
        db.session.commit()

    @staticmethod
    def atualizar_configuracao(local):
        configuracao = Config.query.first()
        if configuracao:
            configuracao.local = local
            db.session.commit()
    
    @staticmethod
    def get_all():
        return Config.query.all()
    
    def __repr__(self):
        return f'<Config {self.local}>'
    