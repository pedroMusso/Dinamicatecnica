from comandos import *

def menu():
    while True:
        print("Protótipo Sistema Terminal Rosa's Consultoria, o que deseja?\n",
        "(1)Cadastrar Consultor\n",
        "(2)Cadastrar Cliente\n",
        "(3)Criar Contrato\n",
        "(4)Visualizar Consultores\n",
        "(5)Visualizar Contratos\n",
        "(s)Sair do Sistema\n")
        inp = input()
        if inp == '1':
            post_consultor()
        elif inp == '2':
            put_cliente()
        elif inp == '3':
            get_contrato()
        elif inp == '4':
            get_consultores()
        elif inp == '5':
            get_consultor()
        elif inp == 's':
            break
        else:print('Comando Inválido')

#print(menu())
menu()