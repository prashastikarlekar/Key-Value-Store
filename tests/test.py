from socket import *
import sys
import time

server = 'localhost'
port = int(sys.argv[1])
c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("TEST FILE TO CONNECT MULTIPLE CLIENTS TO THE SERVER")
print("Starting client to Set value for key \"test1\"\n")
command1 = "set test1 5 \r\n"
c.send(command1.encode())
time.sleep(0.01)
command1_value = "test1" 
c.send(command1_value.encode())
status = c.recv(9542).decode()
print(status)
print("Ending connection for Set Operation\n")
c.close()

c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("Starting client to Get value for key \"test1\"\n")
command2 = "get test1"
c.send(command2.encode())
get_result = c.recv(9542).decode()
print(get_result)
get_end = c.recv(9542).decode()
print(get_end)
c.close()

c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("Starting client to Set value for key \"test2\"\n")
command1 = "set test2 5 \r\n"
c.send(command1.encode())
time.sleep(0.01)
command1_value = "test2" 
c.send(command1_value.encode())
status = c.recv(9542).decode()
print(status)
c.close()

c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("Starting client to Get value for key \"test2\"\n")
command2 = "get test2"
c.send(command2.encode())
get_result = c.recv(9542).decode()
print(get_result)
get_end = c.recv(9542).decode()
print(get_end)
print("Ending connection for Get Operation\n")
c.close()