from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, 
          version='1.0', 
          title='Minha API',
          description='Documentação da API com cadastro',
          doc='/' 
)

# Definimos o modelo para o Swagger exibir o formulário JSON corretamente
user_model = api.model('Usuario', {
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='E-mail do usuário')
})

@api.route("/mensagem")
class Mensagem(Resource):
    def get(self):
        """Retorna a mensagem de boas-vindas"""
        return {"mensagem": "Ola, mundo!"}

@api.route("/usuarios")
class Usuarios(Resource):
    @api.expect(user_model) # Diz ao Swagger para esperar o modelo de usuário
    def post(self):
        """Cadastra um novo usuário"""
        dados = api.payload  # Captura o JSON enviado
        # Aqui entraria a lógica de salvar no banco de dados
        return {
            "status": "sucesso",
            "usuario_criado": dados
        }, 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
