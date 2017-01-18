# -*- coding: UTF-8 -*-
from flask import Flask

def error_response():
    response = jsonify({'message': 'Not allowed'})
    response.status_code = 403
    return response
