#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This file contains endpoints for the service.
"""
import logging
from flask import Blueprint
from flask import current_app
from flask import request
from flask import jsonify
#from flask import Flask, Blueprint, jsonify, current_app, request


# Bit icky - could do with an enum
HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400

v1api = Blueprint('v1', 'v1api') # Create a versioned API

@v1api.route('/status')
def app_status():
    return jsonify(state='ok', message=current_app.service_config), HTTP_200_OK

@v1api.route('/query', methods=['POST'])
def query():
    if not request.data:
        logging.error("No data in request")
        return jsonify({}), HTTP_400_BAD_REQUEST

    data = request.data.decode('ascii')

    logging.info("Params %s : %s", type(data), data)

    return jsonify(results=data), HTTP_200_OK
