def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Phillipe', 'Cláudio', 'Renato']


for i, cliente in enumerate(clientes):
    if i == 2:
        continue
    envia_email(cliente)