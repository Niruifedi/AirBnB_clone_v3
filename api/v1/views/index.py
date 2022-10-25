#!/usr/bin/python3
"""
Script defines url route for the blueprint object
"""


from crypt import methods
from pickle import GET
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_code():
    """
    the url path /status returns a status code 'OK' in json format
    """
    # status = {
    #     'status' : 'OK'
    # }
    return jsonify({"status": "OK"})
