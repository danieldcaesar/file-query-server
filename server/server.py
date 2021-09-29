import socket

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.bind(ADDR)


def start():
    host.listen(1)
    while True:
        conn, addr = host.accept()
        print(f"[NEW CONNECTION] client {addr} is connected.")

        conn.send(bytes(f'[CONNECTED] Connected to server with {addr}', FORMAT))
        conn.close()
    return


print("[STARTING] Server is starting...")
start()