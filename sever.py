import socket
svrSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# svrSkt is short for serverSocket
svrSkt.bind(('127.0.0.1', 1234))  # OR svrSkt.bind(('localhost', 1234))
svrSkt.listen(1)  # queue of 5

connectionSocket, address = svrSkt.accept()
print(f"Connection from {address} has been established!")
connectionSocket.send(bytes("Welcome to the server!", "utf-8"))

while True:
    x = connectionSocket.recv(1024)
    if len(x) <= 0:
        break

    # convert to int
    x = int(x)
    # x**9
    result = x**9
    # convert to string and send
    result_str = str(result)
    print(result_str)
    capitalizedSentence = result_str.upper()
    connectionSocket.send(bytes(capitalizedSentence, "utf-8"))
    print(capitalizedSentence)

connectionSocket.close()
