from socket import *
serverPort = 1200
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "The server is ready to receive"
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print "Received " + message + " from " + clientAddress
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)
