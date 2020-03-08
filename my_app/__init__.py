from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder="templates")

#Database
app.config["MONGO_URI"] = "mongodb://localhost:27017/localdb"
mongo = PyMongo(app)

#import de rotas 
from my_app.api.controller import api
from my_app.core.controller import core

#Registro de controllers
app.register_blueprint(api)
app.register_blueprint(core)


