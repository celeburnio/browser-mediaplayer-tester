# myapp/util/assets.py

from flask_assets import Bundle, Environment
from app import app

bundles = {
    'app_js': Bundle(
        'js/app.js',
        output='js/app.js'),
    'main_css': Bundle(
        'css/main.css',
        output='css/main.css'),
    'bootstrap_css': Bundle(
        'css/bootstrap.min.css',
        output='css/bootstrap.min.css')
}

assets = Environment(app)

assets.register(bundles)