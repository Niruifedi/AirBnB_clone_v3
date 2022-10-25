#!/usr/bin/python3
"""
Script uses blueprint object for routing the application
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    function closes the db when called
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
