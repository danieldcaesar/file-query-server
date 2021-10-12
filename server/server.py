import socket
import glob

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
BUFFER = 4096
SEPARATOR = '<SEPARATOR>'
MSG =''


def put():
    filename = conn.recv(BUFFER).decode(FORMAT)
    file = open(f'{filename}', 'wb')
    data = conn.recv(BUFFER)
    file.write(data)
    file.close()
    print(f'[RECEIVED] Received file \'{filename}\'')

def create():
    print('[WAIT] File being added to server...')
    received = conn.recv(BUFFER).decode()
    filename, data = received.split(SEPARATOR)
    file = open(f'{filename}', 'a')
    file.write(data)
    file.close()
    print(f'[CREATED] File \'{filename}\' created in server.')

def lists():
    files = str(glob.glob('*'))
    data = bytes(files, FORMAT)
    conn.send(data)
    print('[SENT] List of files on server sent.')


def show():
    print('[WAIT] File to be found in server...') 
    #Requested file
    filename = host.recv(BUFFER).decode(FORMAT)
    #if file '!found'
    if not os.path.isfile(filename):
        print('File does not exist.')
        host.send(bytes(MSG,FORMAT))
    #if file 'found'
    file = open(f'{filename}', 'rb')
    #Read entire file
    while True :
        data = file.read(BUFFER)
        host.send(bytes(data,FORMAT))



def delete():
    print('[WAIT] File to be found in server...') 
    #Requested file
    filename = host.recv(BUFFER).decode(FORMAT)
    #if file 'found'
    if os.path.isfile(filename):
        MSG = 'File exist.'
        host.send(bytes(MSG,FORMAT))
        os.remove(filename)
        host.send(bytes('{filename} successfully deleted!'))
    #file '!found'
        elif 
            MSG = 'File exist.'
            host.send(bytes(MSG,FORMAT))


def wordCount():   
    print('[WAIT] File to be found in server...') 
    #Requested file
    filename = host.recv(BUFFER).decode(FORMAT)
    #if file '!found'
    if not os.path.isfile(filename):
        print('File does not exist.')
        host.send(bytes(MSG,FORMAT))

    file = open(f'{filename}', 'rb')
    #Read entire file
    while True :
        data = file.read(BUFFER)
        data = data.split()
        for x in data:
            sum+=1
        if sum > 0
            host.send(bytes('{sum} words',FORMAT))
        else
            host.send(bytes('EMPTY FILE',FORMAT))


def search():    
    print('[WAIT] File to be found in server...') 
    #Requested file
    filename = host.recv(BUFFER).decode(FORMAT)
    #if file '!found'
    if not os.path.isfile(filename):
        print('File does not exist.')
        host.send(bytes(MSG,FORMAT))
    #if file 'found' ,Get key
    word = host.recv(BUFFER).decode(FORMAT)

    file = open(f'{filename}', 'rb')
    #Read entire file
    while True :
        data = file.read(BUFFER)
        data = data.split()
        for x in data:
            if x == "banana":
                host.send(bytes('FOUND {word}',FORMAT))
                break 
        else
            host.send(bytes('{word}NOT FOUND',FORMAT))




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
                lists()
            elif command == 'SHOW':
                show()
            elif command == 'DELETE':               
                delete()
            elif command == 'WORDCOUNT':
                wordCount()
            elif command == 'SEARCH':
                search(command)
    


conn.close()
