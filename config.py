import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    #Secrect KEY
    SECRET_KEY = 'SecretKey'

    # Configuração da pasta de Upload

    upload_folder = os.path.join(basedir,'app', 'static', 'anuncios')
    os.makedirs(upload_folder, exist_ok=True)
    UPLOAD_FOLDER = upload_folder

    # Configuração do Banco de Dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 2 * 1024 * 1024 * 1024  # 2GB