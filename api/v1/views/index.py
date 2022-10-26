#!/usr/bin/python3
"""
Script defines url route for the blueprint object
"""

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_code():
    """
    the url path /status returns a status code 'OK' in json format
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/')
def retrieve_obj():
    """
    retrieves number of object by type
    """
    classes = {"amenities": Amenity, "cities": City, "places": Place,
           "reviews": Review, "states": State, "users": User}

    num_obj = {}
    for key, val in classes.items():
        num_obj[key] = storage.count(val)
    return num_obj
