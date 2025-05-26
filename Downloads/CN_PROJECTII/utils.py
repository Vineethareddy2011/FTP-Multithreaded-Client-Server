import os
import socket

BUF_SIZE = 1024
FORMAT = "utf-8"
DIR = 'data'

def ensure_directory():
    if not os.path.exists(DIR):
        os.makedirs(DIR)

def sendFile(fileName: str, connection: socket.socket, prefix: str) -> None:
    ensure_directory()
    filePath = os.path.join(DIR, fileName)
    if not os.path.exists(filePath):
        connection.send("File does not exist".encode(FORMAT))
        return

    connection.send(f"SIZE {os.path.getsize(filePath)}".encode(FORMAT))
    with open(filePath, 'rb') as file:
        while (data := file.read(BUF_SIZE)):
            connection.sendall(data)

def receiveFile(fileName: str, connection: socket.socket, prefix: str) -> None:
    ensure_directory()
    newFileName = os.path.join(DIR, f"{prefix}{fileName}")
    file_size = int(connection.recv(1024).decode(FORMAT).split()[1])
    with open(newFileName, 'wb') as file:
        total_received = 0
        while total_received < file_size:
            data = connection.recv(BUF_SIZE)
            file.write(data)
            total_received += len(data)

if __name__ == "__main__":
    # Testing can be added here if needed
    pass
