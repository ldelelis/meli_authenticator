import os
from flask import Flask

app = Flask(__name__)

from meli_auth.views import meli_views

app.register_blueprint(meli_views, url_prefix=os.environ.get('MELI_AUTH_ROOT_URL'))
