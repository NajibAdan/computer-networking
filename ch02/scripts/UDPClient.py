from socket import *
serverName = gethostbyname(gethostname())
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Input lowercase sentence:")
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()