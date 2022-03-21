from http import server
from socket import *
import sys
import time

server = 'localhost'
port = int(sys.argv[1])
c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("INITIATING CLIENT REQUEST WITH AN INVALID KEY")
command1 = "set cont\nrol 5 \r\n"
c.send(command1.encode())
time.sleep(0.01)
command1_value = "test1" 
c.send(command1_value.encode())
status = c.recv(9542).decode()
print(status)
print("Ending connection for Set Operation\n")
c.close()