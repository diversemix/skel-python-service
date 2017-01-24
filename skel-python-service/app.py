#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Module initialisation for the flask application.
"""
import json
import api

from flask import Flask
from logger import initLogger

# We need to fix some constants, tho could be passed in as args
SERVICE_CONFIG = '/etc/skel-python-service/config.json'
LOG_PATH = '/etc/service.log'

initLogger(LOG_PATH)

def create_app():
    """ Function that initialises the application from the config. """
    _app = Flask(__name__)

    # TODO
    #_app.config.from_json(CONFIG)

    _app.service_config = {}
    with open(SERVICE_CONFIG) as data_file:
        _app.service_config = json.load(data_file)

    print json.dumps(_app.config,
                    sort_keys=True,
                    indent=4,
                    default=str,
                    separators=(',', ': '))

    return _app

# ----- Main function that runs the application

if __name__ == '__main__':
    app = create_app() # Create the application
    app.register_blueprint(api.v1api, url_prefix='/v1')
    app.run(host="0.0.0.0", port=5000)
