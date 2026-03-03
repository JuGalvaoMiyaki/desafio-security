import pytest
from app import app

def test_mensagem():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.get_json() == {"mensagem": "Ola, mundo!"}

    