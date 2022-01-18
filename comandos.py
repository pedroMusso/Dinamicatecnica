from classes import Cliente,Consultor

s=None
contratos =[]
clientes = []
consultores = []

#Bloco de funções do Menu principal
def post_consultor():
    username = input("Username\n")
    password = input("Password\n")
    print("Consultor adicionado ao sistema!")
    consultores.append(username)
    return None

def put_cliente():
    username = input("Username\n")
    password = input("Password\n")
    clientes.append(username)
    print("Consultor adicionado ao sistema!")
    return None
          
def get_contrato():
    title = input("Title\n")
    description = input("Description\n")
    end_period = input("End Period\n")
    cliente = input("nome do cliente\n")
    consultores = input("nome do consultor\n")

    if len(clientes)==0 or len(consultores)==0:
        print("Não há clientes e/ou consultores cadastrados.")
        return None
    else:
        cliente = clientes.keys(input('Id do cliente:\n'))
        consultor = consultores.keys(input('Id do consultor:\n'))
    associates = f'nome do cliente e {cliente} e o nome do consultor e {consultor}'
    contrato = contratos(title,description,associates)
    contratos.append(contrato)
    print("Contrato adicionado ao sistema!")
    return None

def put_contrato():
    try:contrato = contratos[input("Id do Contrato:\n")]
    except KeyError:
        print("Não existe contrato com esse id")
    contrato.conclude_contract()

def get_consultores():
    print("Consultor Log")
    for i in range(len(consultores)):
        print(consultores[i])
    print("----------------------------")

def get_consultor():
    print("Consultor Log")
    id = int(input("Id do consultor"))
    consultores[id]
    print("----------------------------")