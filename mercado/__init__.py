from flask import Flask, render_template  
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = '010d80d71cd1b357d38a9e20'
db.init_app(app)
bcrypt=Bcrypt(app)
login_manager.init_app(app)
from mercado import routes
