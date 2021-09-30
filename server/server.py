import socket

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
BUFFER = 4096
SEPARATOR = '<SEPARATOR>'



def put():
    filename = conn.recv(BUFFER).decode(FORMAT)
    file = open(f'server/{filename}', 'wb')
    data = conn.recv(BUFFER)
    file.write(data)
    file.close()
    print(f'[RECEIVED] Received file \'{filename}\'')

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
                print('[EXIT] Client has ended connection.')
                connected = False
                break
            if command == 'PUT':
                put()

conn.close()
