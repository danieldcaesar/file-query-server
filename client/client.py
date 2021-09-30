import socket

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
BUFFER = 4096



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True
msg = client.recv(BUFFER)
print(msg.decode())

data = input("Enter the name of a text file eg. PUT sample.txt: ")
filename = data[4:]
client.send(bytes(filename, FORMAT))
file = open(filename, 'rb')
data = file.read(BUFFER)

while data:
    client.send(data)
    data = file.read(BUFFER)

print(f'[SENT] File \'{filename}\' sent.')




client.close()