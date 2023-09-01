from flask import request, jsonify, redirect, Blueprint
import json
from api.utility import say_hello

bp = Blueprint('routes', __name__)

@bp.route('/')
def redirect_to_endpoints():
    return redirect('http://127.0.0.1:8001/api/endpoints/')


@bp.route('/swagger.json')
def swagger():
    """Show documentation page"""
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))
    
@bp.route('/hello', methods=['GET'])
def hello():
    """Say generic hello"""
    return say_hello()

@bp.route('/api/rest_v1/hello', methods=['GET'])
def hello_world():
    """Say hello with an API call"""
    name = request.args.get('name', default='Steve')
    return f"hello, {name}!"