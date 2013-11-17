import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
#from config import basedir

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
#oid = OpenID(app, os.path.join(basedir, 'tmp'))
import views