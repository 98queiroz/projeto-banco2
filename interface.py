#futuramente melhorar a tela de login com comprimento de senha
import os
import time
from funcoes_banco import escreve_tela, procura_user, carregar_contas

#dados do usuario local
login_usuarios = {'login':'queiroz', 'senha':1234}
#carregando as contas dos usuarios
pessoas = carregar_contas()


def tela_login():
    cont = 0
    while True:
        try:
            usuario = str(input('\033[33mDigite seu login: \033[m')).lower().strip()
            senha = int(input('\033[33mDigite sua senha: \033[m').strip())

            if usuario == login_usuarios['login'] and senha == login_usuarios['senha']:
                print(f"\033[36mBem vindo Gerente: {login_usuarios['login']}\033[m")
                time.sleep(2)
                os.system('cls')
                escreve_tela(gerente=True)
                break
            
            else:
                bool = procura_user(pessoas,usuario,senha)
                if bool == False:
                    print('\033[31mfavor digitar login e senha corretamente!\033[m')
                    cont += 1
                    if cont == 3:
                        print('ATÉ BREVE....')
                        break 

        except ValueError:
            print('digite apenas texto sem caracter especiais.')
            continue
        except KeyboardInterrupt:
            print('-- ATÉ LOGO! --')
            break


tela_login()