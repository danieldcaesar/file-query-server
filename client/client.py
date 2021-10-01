import socket

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
    if command[:3] == 'PUT':
        client.send(bytes('PUT', FORMAT))
        put(command)
    if command[:6] == 'CREATE':
        client.send(bytes('CREATE', FORMAT))
        create(command)

client.close()

