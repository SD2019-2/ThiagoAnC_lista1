import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()

    #  Funcoes
    if "salario" in str(message):
        aux = str(message)
        cod,nome,cargo,sal = aux.split(",")

        print (" ")
        print ("Nome: " + nome)
        print ("Cargo: " + cargo)

        if cargo is "operador":
            print ("Salario: " + sal*1.2)
        if cargo is "programador":
            print ("Salario: " + sal*1.18)

    if "maior" in str(message):
        print ("Sera que deu")
    
    if "notas" in str(message):
        print ("Sera que")
    
    if "peso" in str(message):
        print ("Sera")

    if "categ" in str(message):
        print ("Ser")

    if "liquid" in str(message):
        print ("Se")

    if "aposenta" in str(message):
        print ("S")

    if "banco" in str(message):
        print ("bom")

    if "carta" in str(message):
        print ("deu")

    if "stop" in str(message):
        break

    #  Send reply back to client
    socket.send_string("Ola")
