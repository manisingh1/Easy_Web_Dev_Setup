from flask import jsonify
from api import create_cache

### Params ###
cache = create_cache()

def say_hello():
    """ Validate full date input"""
    return jsonify("hello, world!")