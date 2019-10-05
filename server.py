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
    #code here is the function you do want to use, in this case, is "income"
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
                socket.send_string(name + " has not yet come of age!")
            else:
                socket.send_string(name + " came of age!")

        elif "female" in gender:
            if int(age) < 21:
                socket.send_string(name + " has not yet come of age!")
            else:
                socket.send_string(name + " came of age!")

        else:
            socket.send_string("Invalid format!")
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
                socket.send_string("You passed the course!")

            else:
                #print("Reprovado!")
                socket.send_string("You not passed the course!")
        else:
            #print("Reprovado!")
            socket.send_string("You not passed the course!")

        print ("Done!")
        print("-------------")
    
    
    #The message format is
    # (code,height,gender) separated with commas,w/o white spaces
    # code here is "weight"
    if "weight" in str(message):
        aux = str(message)
        cod,height,gender = aux.split(",")
        height,escape = height.split("'")

        height = float(height)

        if "female" in gender:
            socket.send_string("Recommended weight: " + str(round(height*62.1-44.7,2)))
        elif "male" in gender:
            socket.send_string("Recommended weight: " + str(round(height*72.7-58,2)))
        else:
            socket.send_string("Invalid format!")
        print ("Done!")
        print("-------------")


    #The message format is
    # (code,age) separated with commas,w/o white spaces
    # code here is "categ"
    if "categ" in str(message):
        aux = str(message)
        cod,age = aux.split(",")
        age,escape = age.split("'")

        age = int(age)

        if age < 5:
            socket.send_string("Idade insuficiente") # Not enough age to swim
        elif age <= 7:
            socket.send_string("Infantil A") #Child 1
        elif age <= 10:
            socket.send_string("Infantil B") #Child 2
        elif age <= 13:
            socket.send_string("Juvenil A") #Teen 1
        elif age <= 17:
            socket.send_string("Juvenil B") #Teen 2
        elif age >= 18:
            socket.send_string("Adulto")    #Adulto
        else:
            socket.send_string("Invalid age!")
        print ("Done!")
        print("-------------")

    #The message format is
    # (code,name,level,gross,depend) separated with commas,w/o white spaces
    #code here is "net"
    if "net" in str(message):
        aux = str(message)
        cod,name,level,gross,depend = aux.split(",")
        depend,escape = depend.split("'")

        gross = float(gross)

        if "a" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.92)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.97))
        
        elif "b" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.9)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.95))
        
        elif "c" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.85)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.92))

        elif "d" in level:
            if int(depend) != 0:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.83)) 
            else:
                socket.send_string("Name: " + name + " Level: " + level + " Salario liquido: " + str(gross*0.9))

        else:
            socket.send_string("Invalid data!")
        print("Done!")
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

    if "stop" in str(message):
        break
