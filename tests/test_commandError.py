from socket import *
import sys
import time

server = 'localhost'
port = int(sys.argv[1])
c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("INITIATING A CLIENT REQUEST WITH INCORRECT COMMAND PROTOCOL")
command1 = "edit cmdError 8\r\n"
c.send(command1.encode())
time.sleep(0.01)
command1_value = "Wrong command passed"
c.send(command1_value.encode())
status = c.recv(9542).decode()
print(status)
print("Ending connection for Set Operation\n")
c.close()