
def cadastrar_usuario():
    nome = input('Digite seu nome: ')
    idade = input('Qual sua idade? ')
    email = input('Coloque um email para contato: ')  

    u_cadastrados = {
        'nome' : nome,
        'idade' : idade,
        'email' : email,
}
    return u_cadastrados
    

def listar_usuarios(usuarios):
    if len(usuarios) == 0:
        print('Nenhum usuário cadastrado.')
        return

    print('Usuários cadastrados:')
    for u in usuarios:
        print(f"{u['nome']} | {u['idade']} | {u['email']}")
        
def procurar_usuario(usuarios):
    nome_busca = input('Digite o nome que deseja: ')
    for u in usuarios:
        if u['nome'].lower() == nome_busca.lower():
            print ('usuario encontrado')
            print(f"{u['nome']}")
            return True
    return False

