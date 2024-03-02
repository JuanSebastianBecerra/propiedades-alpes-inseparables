import os
from flask import Flask
import threading

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_handlers():
    import src.mercadoalpes.modulos.mercado.aplicacion

def importar_modelos_alchemy():
    pass

def comenzar_consumidor():
    import threading
    import src.mercadoalpes.modulos.mercado.infraestructura.consumidores as mercado

    # Suscripción a eventos
    threading.Thread(target=mercado.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=mercado.suscribirse_a_comandos).start()

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database2.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'ef66b23d-bf07-4eb5-a8ea-1d6262bbc703'
    app.config['SESSION_TYPE'] = 'filesystem'

     # Inicializa la DB
    from src.mercadoalpes.config.db import init_db
    init_db(app)

    from src.mercadoalpes.config.db import db

    importar_modelos_alchemy()
    importar_handlers()

    from . import mercado

    app.register_blueprint(mercado.bp)

    with app.app_context():
        db.create_all()
        comenzar_consumidor()
    
    @app.route("/health-status")
    def health():
        return {"status": "up"}

    return app