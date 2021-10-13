import socket
import os.path
from os import path

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
BUFFER = 4096
SEPARATOR = '<SEPARATOR>'

def exit():
    client.send(bytes('EXIT', FORMAT))

def put(cmd):
    filename = cmd[4:]
    client.send(bytes(filename, FORMAT))
    file = open(filename, 'rb')
    data = file.read(BUFFER)
    while data:
        client.send(data)
        data = file.read(BUFFER)

    print(f'[SENT] File \'{filename}\' sent.')

def create(cmd):
    filename = cmd[7:]
    data = input(f'Enter the contents of file \'{filename}\': ')
    client.send(bytes(f'{filename}{SEPARATOR}{data}', FORMAT))

def lists():
    list = client.recv(BUFFER).decode()
    print(f'[RECEIVED] Files on server: {list}')


def show(cmd):
    filename = cmd[4:]
    #Request file
    client.send(bytes(filename,FORMAT))
    #if file 'found /not found'
    
    #Recieve data from Server
    data = client.recv(BUFFER)
    print(data)


def delete(cmd):
    filename = cmd[6:]
    #Request file
    client.send(bytes(filename,FORMAT))
    #if file 'found /not found'
    data = client.recv(BUFFER).decode(FORMAT)
    print(data) 
    #Recieve data from Server
    data = client.recv(BUFFER).decode(FORMAT)
    print(data)

def wordCount(cmd):
    filename = cmd[9:]
    #Request file
    client.send(bytes(filename,FORMAT))
    #if file 'found /not found'
    client.recv(bytes())
    #Recieve data from Server
    data = client.recv(BUFFER).decode(FORMAT)
    print(data)


def search(cmd):    
    filename = cmd[6:]
    #Request file
    client.send(bytes(filename,FORMAT))
    #status 'found /not found'
    
    #Request word
    word = input(f'Enter the word to search in the file \'{filename}\': ')
    client.send(bytes(word, FORMAT))

    #Recieve data from Server
    data = client.recv(BUFFER).decode(FORMAT)
    print(data)





client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True
msg = client.recv(BUFFER)
print(msg.decode())


while connected:
    command = input("Enter command to be executed: ")
    if command == 'EXIT':
        exit()
        connected = False
    elif command[:3] == 'PUT':
        if path.exists(command[4:]):
            client.send(bytes('PUT', FORMAT))
            put(command)
        else:
            print('[NOTE] File does not exist on client side.')
    elif command[:6] == 'CREATE':
        client.send(bytes('CREATE', FORMAT))
        create(command)
    elif command[:4] == 'LIST':
        client.send(bytes('LIST', FORMAT))
        lists()
    elif command[:7] == 'DELETE':
        client.send(bytes('DELETE', FORMAT))
        delete()        
    elif command[:9] == 'WORDCOUNT':
        client.send(bytes('WORDCOUNT', FORMAT))
        wordCount()
    elif command[:6] == 'SEARCH':
        client.send(bytes('SEARCH', FORMAT))
        search()

client.close()

