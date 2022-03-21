from http import server
from socket import *
import sys
import time

server = 'localhost'
port = int(sys.argv[1])
c = socket(AF_INET, SOCK_STREAM)
c.connect((server,port))
print("INITIATING CLIENT REQUEST TO PASS MULTIPLE KEYS TO THE GET COMMAND WHERE ONE KEY DOESN'T EXISTS IN THE DATABASE")
command2 = "get test1 invalidKey test2"
c.send(command2.encode())
getCommand = command2.split()
for i in range(1,len(getCommand)):
        get_result = c.recv(9542).decode()
        print(get_result)
get_end = c.recv(9542).decode()
print(get_end)
print("Ending connection for Get Operation\n")
c.close()