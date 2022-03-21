#!/usr/bin/env python3
import socket
import sys, time

HOST = "localhost"
# PORT= 9889
PORT =  int(sys.argv[1])        # The port used by the server

def getItem(cmd1,c):
    getcmd= cmd1.split()
    for i in range(1,len(getcmd)):
        res = c.recv(9542).decode()
        print(res)
    print(c.recv(9542).decode())

def setItem(cmd1,c):
    # value = input("Enter the value of the key : ")
    value = input()
    if not value:
        print("CLIENT_ERROR PROTOCOL WAS NOT FOLLOWED")
        c.close()
    c.send(value.encode())
    status= c.recv(9542).decode()
    print(status)
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    # cmd1 = input("Enter the operation :\n")
    cmd1 = input()
    c.send(cmd1.encode())
    # print(f"The type of data being sent is {type(cmd1)} and the data is {cmd1}")
    if cmd1[:3] == "set":
        setItem(cmd1,c)
    elif cmd1[:3] == "get":
        getItem(cmd1,c)
    else:
        error =c.recv(9542).decode()
        print(error)
    c.close()




