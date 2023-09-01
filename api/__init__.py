from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import redis
from flask_cors import CORS

def create_app():
    """ Create and configure the Flask app instance. """
    app = Flask(__name__)

    # allow localhost and http://127.0.0.1/ both to work
    CORS(app)

    # Configure Swagger UI for documentation
    SWAGGER_URL = '/api/endpoints'
    API_URL = 'http://localhost:8001/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Sample API"
        }
    )
    
    from api import routes
    app.register_blueprint(routes.bp)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app

def create_cache():
    # Configure redis for caching requests
    cache = redis.Redis(host='redis', port=6379)
    return cache