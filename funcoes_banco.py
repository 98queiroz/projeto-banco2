from typing import List, Dict
from banco import carregar_contas

pessoas = carregar_contas()

def escreve_tela(gerente=False, cliente=False):
    if gerente == True:
        print()
        print(' MENU PERFIL GERENTE')
        print('*******Banco do Povo*******')
        print('1 - abrir conta')
        print('2 - atualizar dados')
        print('3 - encerrar conta')
        print('0 - sair')
        print()
        
    
    if cliente == True:
        print()
        print(' MENU PERFIL CLIENTE')
        print('*******Banco do Povo*******')
        print('1 - Consultar extrato')
        print('2 - realizar deposito')
        print('3 - realizar saque')
        print('4 - realizar emprestimo')
        print('5 - consultar emprestimo')
        print('0 - sair')
        print()
    
def procura_user(pessoas: List[Dict[str,str]], usuario:str, senha:int)-> dict[str,str]:
    for user in pessoas:
        print
        """ if usuario == user['login'] and senha == user['password']:
            print(f"\033[36mBem vindo Cliente: {usuario['login']}\033[m")
            escreve_tela(cliente=True)
        else:
            return False """

c = carregar_contas()
procura_user(c,'matheus',1234)



def abrir_conta():...
    #cadastrar  usuario

def atualizar_dados():...
    #pesquisar no dicionario

def encerrar_conta():...
    #criar o dicionario

def consulta_extrato():...
    #cadastrar todos esses dados do usuario

def realizar_deposito():...
    #verificar se está negativo

def realizar_emprestimo():...
    #aqui o usuario deve ter um limite

def consulta_emprestimo():...
    #consultar o emprestimo da pessoa