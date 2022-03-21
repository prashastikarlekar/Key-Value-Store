#!/usr/bin/env python3
import socket
import os, sys
import json

HOST = "localhost"  # Standard loopback interface address (localhost)
# PORT = 9889        # Port to listen on (non-privileged ports are > 1023)

PORT = int(sys.argv[1])

# path=os.getcwd()
# os.chdir(path+'\MyAssignment')

def getItem(key):
    for k in key[1:]:
        try:
                # with open(os.getcwd()+'\data\\' +(str(k)+'.json'),'r') as fr:
                with open('data\\' +(str(k)+'.json'),'r') as fr:
                    data = json.load(fr)
                conn.send(("VALUE "+str(k)+" "+str(len(data[k]))+" \r\n"+data[k]+ "\r\n").encode())
        except FileNotFoundError:
            pass

def setItem(key):
    if not(isValidKey(key[1])):
            return "CLIENT_ERROR INVALID KEY\r\n".encode()
    else:
        value = conn.recv(9542).decode()        
        if int(key[2]) != len(value):
            return 'CLIENT_ERROR : THE LENGTH OF THE VALUE DO NOT MATCH.\r\n'.encode()
        elif len(key) != 3:
            return 'CLIENT_ERROR: COMMAND PROTOCOL WAS NOT FOLLOWED.\r\n'.encode()
        else:
            try:
                with open('data\\' +(str(key[1])+'.json'),'w') as fw:
                    data = {key[1]:value}
                    json.dump(data, fw)
                    return "STORED\r\n".encode()
            except Exception:
                return "NOT_STORED\r\n".encode()

def isValidKey(key):
    if not key.isalnum() or len(key) > 250:
        # print("Invalid key.")
        return False
    return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as myServer:
    try:
        myServer.bind(('', PORT))
        myServer.listen(1)
        print("Started listening")
        while True:
            conn, addr = myServer.accept()
            # with conn:
            print('Connected by', addr)
            # while True:
            cmd1 = conn.recv(9542).decode()
            data= cmd1.split()

            if data[0] == "set":
                res = setItem(data)
                conn.send(res)
            elif data[0] == "get":
                print(f"The data passed to get is {data}")
                result = getItem(data)
                conn.send('END\r\n'.encode())
                # conn.close()
            else:
                conn.send('ERROR\r\n'.encode())
    except Exception as e:
            conn.send('ERROR OCCURED\r\n'.encode())
