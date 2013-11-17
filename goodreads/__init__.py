#import os
from flask import Flask
from flask.ext.login import LoginManager
from goodreads import settings
#from flask.ext.openid import OpenID
#from config import basedir

app = Flask(__name__, static_folder='./static',
                template_folder='./templates')
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(settings)
#oid = OpenID(app, os.path.join(basedir, 'tmp'))
import views