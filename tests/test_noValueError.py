from socket import *
import sys
import time

server = 'localhost'
port = int(sys.argv[1])
c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("INITIATING CLIENT REQUEST WITH WRONG SET COMMAND PROTOCOL : NO VALUE IS PASSED")
command1 = "set setError \r\n"
c.send(command1.encode())
time.sleep(0.01)
command1_value = "PROTOCOL ERROR"
c.send(command1_value.encode())
status = c.recv(9542).decode()
print(status)
print("Ending connection for Set Operation\n")
c.close()