import socket
# https://www.youtube.com/watch?v=Lbfe3-v7yE0
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))

s.listen(5) # 5 connections at a time (Thi is a Que)

while True:
    clientsocket , address = s.accept()
    print(f"Connection from {address} has been established at {clientsocket}")

    # Maybe add a welcome library
    clientsocket.send(bytes("Welcome Padawan","utf-8"))


def end_server():
    quit()

