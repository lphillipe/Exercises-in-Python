import api

usuario = 'luis'
senha = '1234'

login = api.login(usuario, senha)
print(login)