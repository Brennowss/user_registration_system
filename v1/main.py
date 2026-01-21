from funcoes import cadastrar_usuario, listar_usuarios, procurar_usuario

usuarios = []

while True:
    opcao = input('''
1- Cadastrar usuário
2- Listar usuários
3- Procurar usuário
0- Encerrar programa
''')

    if opcao == '0':
        print('Encerrando programa')
        break


    elif opcao == '1':
        novo_user = cadastrar_usuario()
        usuarios.append(novo_user)
    
    elif opcao == '2':
        listar_usuarios(usuarios)

    elif opcao == '3':
        resultado = procurar_usuario(usuarios)
        print('Usuário encontrado!')
    else:
        print('Não encontrado')