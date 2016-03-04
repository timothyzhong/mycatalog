from flask import Flask
app = Flask(__name__)

import catalog.application

UPLOAD_FOLDER = '/var/www/catalog/catalog/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_FOLDER = '/var/www/catalog/catalog'
app.config['APP_FOLDER'] = APP_FOLDER
