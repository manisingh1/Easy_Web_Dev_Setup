import pytest
from flask import json
import debugpy
from api import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    """ Test redirect to swagger api page"""
    response = client.get('/')
    assert response.status_code == 302