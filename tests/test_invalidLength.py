from socket import *
import sys
import time

server = 'localhost'
port = int(sys.argv[1])
c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("INITAITING CLIENT REQUEST WITH DIFFERENT VALUE THAN THE SPECIFIED")
command1 = "set valueError 8 \r\n"
c.send(command1.encode())
time.sleep(0.01)
command1_value = "WRONG SIZE"
c.send(command1_value.encode())
status = c.recv(9542).decode()
print(status)
print("Ending connection for Set Operation\n")
c.close()