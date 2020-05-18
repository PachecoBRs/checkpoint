from funcoes import *

vazamentos = {"PACHECO":["pachequinho@gmail.com","123123"], "ALBERICO":["alberico@top.com","senhaForte"]}
resp = "S"

while resp == "S":
    print("----------------------------")
    print("|Controle de Emails Vazados|")
    print("----------------------------")
    print("Opção 1 - Cadastro de Emails ")
    print("Opção 2 - Lista de Emails Vazados ")
    print("Opção 3 - Buscar Email  ")
    print("Opção 4 - Alterar Email ")
    print("Opção 5 - Alterar Email ")
    print("Opção 6 - Excluir Email ")
    print("Opção 7 - Sair do Programa ")
    opcao = int(input("Digite o número da opção desejada:"))

    if opcao == 1:
        cadastroEmail(vazamentos)
    elif opcao == 2:
        listarEmails(vazamentos)
    elif opcao == 3:
        buscarEmails(vazamentos)
    elif opcao == 4:
        alterarEmail(vazamentos)
    elif opcao == 5:
        alterarSenha(vazamentos)
    elif opcao == 6:
        excluirEmail(vazamentos)
    elif opcao == 7:
        print("Até logo!")
        break
        

