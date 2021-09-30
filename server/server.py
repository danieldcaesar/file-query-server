import socket
import shutil

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
BUFFER = 4096


def start():
    host.listen(1)
    
    while True:
        conn, addr = host.accept()
        print(f"[NEW CONNECTION] client {addr} is connected.")
        conn.send(bytes(f'[CONNECTED] Connected to server {SERVER}:{PORT}', FORMAT))

        filename = conn.recv(BUFFER).decode(FORMAT)
        file = open(f'server/{filename}', 'wb')
        data = conn.recv(BUFFER)
        while data:
            file.write(data)
            data = conn.recv(BUFFER)
        file.close()
        print(f'[RECEIVED] Received file \'{filename}\'')
        conn.close()
        
        break        

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.bind(ADDR)
print("[START] Server has started.")
start()