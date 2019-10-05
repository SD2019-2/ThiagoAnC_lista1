import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()

    #Functions


    #The message format is 
    # (code,name,job_role,salary) separated with commas,w/o white spaces
    #code here is the function you do want to use, in this case, is income
    if "income" in str(message):
        aux = str(message)
        cod,name,role,sal = aux.split(",")
        sal,escape = sal.split("'")

        if "operador" in role:
            socket.send_string("New income: " + str(float(int(sal)) *1.2))

        elif "programmer" in role:
            socket.send_string("New income: " + str(float(int(sal)) *1.18))

        else:
            socket.send_string("Invalid job role!")
            
        print ("Done!")
        print("-------------")

    
    #The message format is
    # (code,name,gender,age) separated with commas,w/o white spaces
    # code here is "bigger"  
    if "bigger" in str(message):
        aux = str(message)
        cod,name,gender,age = aux.split(",")
        age,escape = age.split("'")

        if "male" in gender:
            if int(age) < 18:
                socket.send_string(nome + " has not yet come of age!")
            else:
                socket.send_string(nome + " came of age!")

        elif "female" in gender:
            if int(age) < 21:
                socket.send_string(nome + " has not yet come of age!")
            else:
                socket.send_string(nome + " came of age!")

        else:
            socket.send_string("We do not have support to your gender, but we accept your choice!")
        print ("Done!")
        print("-------------")


    #The message format is
    # (code,score1,score2.score3) separated with commas,w/o white spaces
    # code here is "score"
    if "score" in str(message):
        aux = str(message)
        cod,n1,n2,n3 = aux.split(",")
        n3,escape = n3.split("'")

        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        if ((n1+n2)/2) >= 7:
            socket.send_string("You passed the course!")

        elif ((n1+n2)/2) >= 3:
            socket.send_string("You have not passed the course yet, you must do the third test!")

            if (((n1+n2)/2) + n3)/3 > 5:
                #print("Aprovado!")
                socket.send_string("Aprovado!")

            else:
                #print("Reprovado!")
                socket.send_string("Reprovado!")
        else:
            #print("Reprovado!")
            socket.send_string("Reprovado!")

        print ("Solicitacao entregue!")
        print("-------------")
    
    if "peso" in str(message):
        aux = str(message)
        cod,altura,sexo = aux.split(",")
        altura,escape = altura.split("'")

        altura = float(altura)

        if "feminino" in sexo:
            socket.send_string("Peso ideal: " + str(round(altura*62.1-44.7,2)))
        elif "masculino" in sexo:
            socket.send_string("Peso ideal: " + str(round(altura*72.7-58,2)))
        else:
            socket.send_string("Sexo invalido")
        print ("Solicitacao entregue!")
        print("-------------")

    if "categ" in str(message):
        aux = str(message)
        cod,idade = aux.split(",")
        idade,escape = idade.split("'")

        idade = int(idade)

        if idade < 5:
            socket.send_string("Idade insuficiente!")
        elif idade <= 7:
            socket.send_string("infantil A")
        elif idade <= 10:
            socket.send_string("infantil B")
        elif idade <= 13:
            socket.send_string("juvenil A")
        elif idade <= 17:
            socket.send_string("juvenil B")
        elif idade >= 18:
            socket.send_string("adulto")
        else:
            socket.send_string("Idade invalida!")
        print ("Solicitacao entregue!")
        print("-------------")

    if "liquid" in str(message):
        aux = str(message)
        cod,nome,nivel,brut,depend = aux.split(",")
        depend,escape = depend.split("'")

        brut = float(brut)

        if "a" in nivel:
            if int(depend) != 0:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.92)) 
            else:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.97))
        
        elif "b" in nivel:
            if int(depend) != 0:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.9)) 
            else:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.95))
        
        elif "c" in nivel:
            if int(depend) != 0:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.85)) 
            else:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.92))

        elif "d" in nivel:
            if int(depend) != 0:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.83)) 
            else:
                socket.send_string("Nome: " + nome + " Nivel: " + nivel + " Salario liquido: " + str(brut*0.9))

        else:
            socket.send_string("Dados invalidos!")
        print("Solicitacao entregue!")
        print("-------------")

    if "aposenta" in str(message):
        aux = str(message)
        cod,idade,servico = aux.split(",")
        servico,escape = servico.split("'")

        if int(idade) >=65 and int(servico) >=30:
            socket.send_string("Pode descansar, a aposentadoria esta aprovada!")
        else:
            socket.send_string("Aguenta um pouco que voce ainda pode ser explorado!")
        print("Solicitacao entregue!")
        print("-------------")
   
    if "banco" in str(message):
        aux = str(message)
        cod,saldo = aux.split(",")
        saldo,escape = saldo.split("'")

        if int(saldo) <= 200:
            socket.send_string("Nao ha credito disponivel para um saldo de " + saldo)
        elif int(saldo) <= 400:
            socket.send_string("Temos 20%. de credito para um saldo de " + saldo)
        elif int(saldo) <= 600:
            socket.send_string("Temos 30%. de credito para um saldo de " + saldo)
        elif int(saldo) > 600:
            socket.send_string("Temos 40%. de credito para um saldo de " + saldo)
        elif int(saldo) < 0:
            socket.send_string("Dados invalidos")
        print("Solicitacao entregue!")
        print("-------------")

    if "carta" in str(message):
        print ("deu")

    if "stop" in str(message):
        break
