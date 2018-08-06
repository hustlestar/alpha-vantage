from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "fuckall"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@database/stock_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/stock_db'

db = SQLAlchemy(app)
#db.create_all()

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
import utils
import os
secrets_path = '../secrets/credentials.properties'
secrets_path = os.path.normpath(secrets_path)
print os.getcwd()
props = utils.read_properties(secrets_path)

from web import routes