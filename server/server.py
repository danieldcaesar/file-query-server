# libraries used
import socket
import glob
import os
import os.path
from os import path


# global variables
PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
BUFFER = 4096
SEPARATOR = '<SEPARATOR>'


# functions
def put():
    filename = conn.recv(BUFFER).decode(FORMAT)
    file = open(filename, 'wb')
    data = conn.recv(BUFFER)
    file.write(data)
    file.close()
    print(f'[RECEIVED] Received file \'{filename}\'')


def create():
    print('[WAIT] File being added to server...')
    received = conn.recv(BUFFER).decode()
    filename, data = received.split(SEPARATOR)
    file = open(filename, 'w')
    file.write(data)
    file.close()
    print(f'[CREATED] File \'{filename}\' created in server.')


def list():
    files = str(glob.glob('*'))
    data = bytes(files, FORMAT)
    conn.send(data)
    print('[SENT] List of files on server sent.')


def show():
    filename = conn.recv(BUFFER).decode(FORMAT)
    if path.exists(filename):
        file = open(filename, 'r')
        data = str(file.read())
        conn.send(bytes(data, FORMAT))
        print(f'[SENT] Client requested file \'{filename}\'')
        file.close()
    else:
        conn.send(bytes('Requested file not found.', FORMAT))
        print(f'[NOTE] Client requested file \'{filename}\'. File not found.')
    

def delete():
    filename = conn.recv(BUFFER).decode(FORMAT)
    if path.exists(filename):
        os.remove(filename)
        print(f'[NOTE] File \'{filename}\' removed.')
        conn.send(bytes(f'[NOTE] File \'{filename}\' removed from server.', FORMAT))
    else: 
        conn.send(bytes('[SERVER] Unable to delete. Requested file not found.',FORMAT))
        print(f'[NOTE] Client requested delete \'{filename}\'. File not found.')


def wordcount():   
    filename = conn.recv(BUFFER).decode(FORMAT)
    if path.exists(filename):
        print(f'[REQUEST] Sent word count for file \'{filename}\'')
        file = open(f'{filename}', 'rb')
        read_data = file.read()
        words = read_data.split()
        num_words = len(words)

        if num_words>0:
            conn.send(bytes(f'[SERVER] Number of words: {num_words}', FORMAT))
        else: 
            conn.send(bytes('[SERVER] Empty file.',FORMAT))

    else:
        conn.send(bytes('[SERVER] File not found.', FORMAT))
        print('[NOTE] Client requested WORDCOUNT on invalid file.')


def search():   
    print('[WAIT] Searching file on server...') 
    received = conn.recv(BUFFER).decode(FORMAT)
    filename, query = received.split(SEPARATOR)
    if path.exists(filename):
        file = open(filename, 'rb')
        read_data = file.read()
        words = str(read_data.split())

        if query in words:
            conn.send(bytes(f'[SERVER] \'{query}\' is in \'{filename}\'', FORMAT))
            print(f'[NOTE] Query on file \'{filename}\' was successful.')
        else:
            conn.send(bytes(f'[SERVER] \'{query}\' is not in \'{filename}\'', FORMAT))
            print(f'[NOTE] Query on file \'{filename}\' was unsuccessful.')

    else:
        conn.send(bytes('[SERVER] File not found.', FORMAT))
        print(f'[NOTE] File queried not found.')



# main execution
host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.bind(ADDR)
print("[START] Server has started.")
host.listen(1)
connected = True
while connected:
        conn, addr = host.accept()
        print(f"[NEW CONNECTION] client {addr} is connected.")
        conn.send(bytes(f'[CONNECTED] Connected to server {SERVER}:{PORT}', FORMAT))

        wait_command = True
        while wait_command:
            command = conn.recv(BUFFER).decode(FORMAT)
            if command == 'EXIT':
                print('[EXIT] Client has terminated connection.')
                connected = False
                break
            elif command == 'PUT':
                put()
            elif command == 'CREATE':
                create()
            elif command == 'LIST':
                list()
            elif command == 'SHOW':
                show()
            elif command == 'DELETE':               
                delete()
            elif command == 'WORDCOUNT':
                wordcount()
            elif command == 'SEARCH':
                search()
conn.close()
