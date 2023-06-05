#!/usr/bin/python3
""" Views implementation. For different end points
"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from models import classes
from models.state import State


@app_views.route('/status', strict_slashes=False)
def status_page():
    """Returns status page with status set to OK
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """Returns stats for every class implemented
    """
    stats = {}
    names = {"State": "states", "City": "cities", "Place": "places",
             "Review": "reviews", "User": "users", "Amenity": "amenities"}
    for key in classes:
        stats[names[key]] = storage.count(classes[key])
    return jsonify(stats)
