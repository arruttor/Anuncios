from flask import Flask, redirect, render_template, request, flash, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .services.base_services import verifica_tabela_criada
from .db import db
from .services.extensions import socketio
import gevent
import gevent.monkey


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    gevent.monkey.patch_all()

    socketio.init_app(app)
    with app.app_context():
        verifica_tabela_criada()


    from app.routes.home_routes import home_bp
    from app.routes.display_routes import disp_bp
    from app.routes.cadastro_routes import cad_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(disp_bp)
    app.register_blueprint(cad_bp)




    return app