def login(usuario, senha):
    if usuario == 'luis' and senha == '1234':
        return 'Login correto, você está logado!'
    else:
        return 'Login incorreto, você foi desconectado!'
    
def envia_email_log():
    return 'Email com log enviado!'