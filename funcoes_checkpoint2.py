vazamentos= []


#Cadastro de Email
def cadastroEmail(leak):
    resp = "S"
    while resp == "S":
        tag = input("Qual a tag do email? ").upper()
        leak[tag] = (input("Qual o email vazado?: "), input("Senha do email: "))
        resp = input("Deseja adicionar mais um email? ").upper()

#Listar emails
def listarEmails(leak):
    for tag, dados in leak.items():
        print("\nTag:", tag)
        print("Email: ",dados[0])
        print("Senha: ",dados[1])
        

#Buscar Email
def buscarEmails(leak):
    busca = input("Digite a tag do email que deseja buscar: ").upper()
    lista = leak.get(busca)
    if lista !=None:
        print("Email: ",lista[0])
        print("Senha: ",lista[1])
    else:
        print("Email não foi vazado ou não foi cadastrado")

#Alterar email
def alterarEmail(leak):
    alteracao = input("Qual a tag do email?: ").upper()
    lista = leak.get(alteracao)
    lista[0] = input("Qual o novo email?: ")
    leak[alteracao] =[lista[0], lista[1]]
    lista = leak.get(alteracao)
    if lista != None:
        print("\nEmail:", lista[0])
        print("Senha:", lista[1])

#Alterar senha
def alterarSenha(leak):
    alteracao = input("Qual a tag do email?: ").upper()
    lista = leak.get(alteracao)
    lista[1] = input("Qual a nova senha?: ")
    leak[alteracao] =[lista[0], lista[1]]
    lista = leak.get(alteracao)
    if lista != None:
        print("\nEmail:", lista[0])
        print("Senha:", lista[1])

#Excluir
def excluirEmail(leak):
    excluir=input("\nDigite a tag do email que deseja excluir: ")
    if leak.get(excluir) != None:
        del leak[excluir]
    print("Email excluído\n")