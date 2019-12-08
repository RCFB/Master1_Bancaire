from flask import Flask
import os

app = Flask(__name__)

app.config.update(SECRET_KEY=os.environ.get('FLASK_SECRET_KEY'))

from . import compte_controller
from . import authent_controller
from . import command_line_interface
