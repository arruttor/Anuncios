from flask import current_app
from sqlalchemy import inspect
from ..db import db
from ..models.Anuncio import Anuncio

def verifica_tabela_criada():
    with current_app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table(Anuncio.__tablename__):
            db.create_all()
            print('Tabela criada')
        else:
            print('Tabela já criada, sem alteração')