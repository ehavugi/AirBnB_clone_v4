#!/usr/bin/python3
"""api/v1 app entry point
   hanlder for api version 1.
"""
from models import *
from models import storage
from models import classes

from flask import Flask, render_template, Blueprint, jsonify
from api.v1.views import app_views
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """JSON 404 error message
    """
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def closeApp(exception=None):
    """ Teardown by closing storage
    """
    storage.close()


if __name__ == "__main__":
    hostname = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = os.environ.get("HBNB_API_PORT", 5000)
    app.run(host=hostname, port=port, threaded=True, debug=True)
