emails = []
resposta = "S"

while resposta == "S":
    emails.append(input("qual o email vazado? "))
    respostawhile = ""
    while respostawhile != "S" and respostawhile != "N":
        respostawhile = input("Deseja adicionar mais um email vazado? ").upper()
        resposta = respostawhile

consulta = input("Digite o email para saber se foi vazado: ")

while consulta in emails:
    print("O email foi vazado :O")
    ask = input("Deseja saber se mais um email foi vazado? ").upper()
    if ask == "N":
        print("ok :)")
        break
    else:
        if ask == "S":
            consulta = input("Digite o email para saber se foi vazado: ")

while consulta not in emails:
    print("O email não foi vazado :D")
    ask = input("Deseja saber se mais um email foi vazado? ").upper()
    if ask == "N":
        print("ok :)")
        break
    else:
        if ask == "S":
            consulta = input("Digite o email para saber se foi vazado: ")
