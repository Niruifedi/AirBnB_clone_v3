#!/usr/bin/python3
"""
Script uses blueprint object for routing the application
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(error):
    """
    function closes the db when called
    """
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """
    404 error handler
    """
    return jsonify({"error": 'Not found'})


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000

    app.run(host=host, port=port, threaded=True)  # type: ignore
