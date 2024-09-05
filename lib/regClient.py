import socket

PORT = 5050
HEADER = 64
SERVER = "localhost"    #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
#print(SERVER)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length+= b' ' * (HEADER - len(send_length))    #Padding
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))

send("Hello Wo uyurld")
send("Hellotrytybt dtudyu dty World")
send("Hello Word u t7ud tutu5487y udyu yuld")
input()
send(DISCONNECT_MESSAGE)