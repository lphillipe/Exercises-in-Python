from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SECRET_KEY'] = 'd57032b601e0868aa8525b06'
db = SQLAlchemy(app)

from market import routes