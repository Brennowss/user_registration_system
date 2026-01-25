from funcoes import cadastrar_usuario, listar_usuarios, procurar_usuario, remover_user, salvar_dados, carregar_txt

usuarios = carregar_txt()

while True:
    opcao = input('''
1- Cadastrar usuário
2- Listar usuários
3- Procurar usuário
4- Remover usuário
0- Encerrar programa
''')

    if opcao == '0':
        print('Encerrando programa')
        break


    elif opcao == '1':
        novo_user = cadastrar_usuario()
        usuarios.append(novo_user)
        salvar_dados(novo_user)
        
    
    elif opcao == '2':
        usuarios = carregar_txt()
        listar_usuarios(usuarios)

    elif opcao == '3':
        resultado = procurar_usuario(usuarios)
        print('Usuário encontrado!')

    elif opcao == '4':
        if remover_user(usuarios):
            print('usuário apagado')
        else:
            print('não apagado')
    
