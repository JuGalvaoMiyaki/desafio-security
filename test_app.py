import pytest
from app import app

def test_mensagem():
    # Ajuste o caminho para a nova rota definida no @api.route
    response = app.test_client().get('/mensagem') 
    assert response.status_code == 200
    assert response.get_json() == {"mensagem": "Ola, mundo!"}

   
