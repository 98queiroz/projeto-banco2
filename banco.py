import os
import json


def carregar_contas():
    lista_contas = []

    if os.path.exists('contasbanco.json'):
        with open('contasbanco.json', 'r') as contas:
            lista_contas = json.load(contas)
        return lista_contas
    else:
        print('-- NENHUMA CONTA CADASTRADA --')
    

    
def guarda_contas(dic_conta):
    with open('contasbanco.json', 'w') as contas:
        json.dump(dic_conta,contas, indent=4)


""" {'nome':'matheus queiroz',
             'cpf':'033.248.402.52',
             'conta_corrente':'44973-3',
             'senha':1234,
             'agencia':2811, 
             'renda':1.200,} """
