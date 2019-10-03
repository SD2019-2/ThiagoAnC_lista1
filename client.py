import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    #print("Sending request %s …" % request)
    questao = input()
    socket.send_string (questao)

    #  Get the reply.
    message = socket.recv()
    print("...")

    if "stop" in questao:
        socket.send_string ("stop")
        break