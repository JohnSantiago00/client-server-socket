import socket
# cltSkt short for clientSocket
cltSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cltSkt.connect(('localhost', 1234))  # ip address and port #

msg = cltSkt.recv(1024)  # buffer size 1024 bytes
print(msg.decode("utf-8"))

while True:
    sentence = input("Input an Integer: ")
    cltSkt.send(bytes(sentence, "utf-8"))
    msgRecvd = cltSkt.recv(1024)
    print('From Server:', msgRecvd.decode("utf-8"))

cltSkt.close()
