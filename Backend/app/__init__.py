from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

    from app.routes.auth import auth_bp
    from app.routes.islands import islands_bp
    from app.routes.creopedia import creopedia_bp
    from app.routes.turnips import turnips_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(islands_bp, url_prefix='/api/islands')
    app.register_blueprint(creopedia_bp, url_prefix='/api/creopedia')
    app.register_blueprint(turnips_bp, url_prefix='/api/turnips')

    return app
