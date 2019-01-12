import os
import sys
from datetime import datetime, timedelta
from flask import render_template, request, Response, Blueprint

from meli_auth import app
from meli_auth.driver import save_user, get_token

# I'd rather not do this but meli's python sdk is garbage
sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
from meli import Meli  # NOQA


meli_client = Meli(client_id=os.environ.get('MELI_AUTH_CLIENT_ID'),
                   client_secret=os.environ.get('MELI_AUTH_CLIENT_SECRET'))
TOKEN_EXPIRY_HOURS = 6


meli_views = Blueprint("meli_views", __name__, template_folder="templates")


def request_token(refresh_token):
    meli_token = meli_client.authorize(
        refresh_token, os.environ.get('MELI_AUTH_CALLBACK_URL'))
    data = {'user_id': meli_client.refresh_token.split('-')[2],
            'access_token': meli_token,
            'refresh_token': meli_client.refresh_token,
            'timestamp': datetime.now()}
    return save_user(data)


@meli_views.route("/")
def index():
    auth_url = meli_client.auth_url(os.environ.get('MELI_AUTH_CALLBACK_URL'))
    return render_template('index.html', auth_url=auth_url)


@meli_views.route("/callback")
def callback():
    if "code" not in request.args:
        return Response(status=500)
    row = request_token(request.args.get("code"))
    return render_template("callback.html", token=row)


@meli_views.route("/<user_id>/token")
def token(user_id):
    user_data = get_token(user_id)
    if not user_data:
        return Response("No User Found", status=404)
    resp_text = user_data["access_token"]
    if user_data['timestamp'] + timedelta(hours=TOKEN_EXPIRY_HOURS) < datetime.now():
        resp_text = request_token(user_data['refresh_token'])
    return Response(resp_text, status=200)
