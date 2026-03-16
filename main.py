import api
import os

usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

login = api.login(usuario, senha)
print(login)