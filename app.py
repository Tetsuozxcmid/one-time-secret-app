from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()


def create_app():
    app = Flask(__name__,template_folder='templates',static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./secretdb.db'
    app.secret_key = 'some key'
    
    db.init_app(app)
    

    from routes import register_routes
    register_routes(app,db)

    migrate = Migrate(app,db,render_as_batch=True)

    return app
