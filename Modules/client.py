import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

# Calculating proper buffer size is the job of the net engineers (Note to self : RIP)
msg = s.recv(1024)
print(msg.decode("utf-8"))

