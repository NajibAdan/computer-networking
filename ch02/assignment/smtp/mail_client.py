from socket import *
import time
import base64

print ""

username = raw_input("Enter your mail.com username : ")
password = raw_input("Enter your mail.com password : ")
rec = raw_input("\nEnter the recipient's email address : ")

name = username.split('@')[0]
subject = "TEST EMAIL"

message = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.mail.com"
mailserverPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailserverPort))

recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send EHLO (for Extended SMTP) command and print server response.
heloCommand = 'EHLO Ashara\r\n'
print 'COMMAND: ' + heloCommand
clientSocket.send(heloCommand)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Authentication required for the mail.com server I'm using
command = 'AUTH LOGIN\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send username as Base64 encoded string
command = base64.b64encode(username) + '\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send password as Base64 encoded string
command = base64.b64encode(password) + '\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send MAIL FROM command and print server response.
command = "MAIL FROM: <" + username + ">\r\n"
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send RCPT TO command and print server response.
command = "RCPT TO: <" + rec + ">\r\n"
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send DATA command and print server response.
command = "DATA\r\n"
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv

# Send message headers
command = 'From: ' + name + ' <' + username + '>' + '\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)
command = 'To: ' + rec + '\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)
command = 'Date: ' + time.asctime( time.localtime(time.time()) ) + '\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)
command = 'Subject: ' + subject + '\r\n'
print 'COMMAND: ' + command
clientSocket.send(command)

# Send message data.
clientSocket.send('\r\n')
for msg in message:
    print 'COMMAND: ' + msg
    clientSocket.send(msg)

# Message ends with a single period.
print 'COMMAND: ' + endmsg
clientSocket.send(endmsg)

# Send QUIT command and get server response.
command = "QUIT\r\n"
print 'COMMAND: ' + command
clientSocket.send(command)
recv = clientSocket.recv(1024)
print 'SERVER RESPONSE: ' + recv