import socket
import utils

IP = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"

def client():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    command = input("Enter command (e.g., ftpclient 8080): ")
    if 'ftpclient ' in command:
        port = int(command.split(' ')[1])
        try:
            connection.connect((IP, port))
            print(f"Connected to {IP}:{port}")
            while True:
                remote_command = input("Enter command (get/upload <FILENAME>, exit): ")
                if remote_command == 'exit':
                    connection.send(remote_command.encode(FORMAT))
                    break
                connection.send(remote_command.encode(FORMAT))
                action, fileName = remote_command.split(' ')
                if action == 'get':
                    utils.receiveFile(fileName=fileName, connection=connection, prefix='new')
                elif action == 'upload':
                    utils.sendFile(fileName=fileName, connection=connection, prefix='new')
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()
            print("Connection closed.")
    else:
        print("Invalid command format.")

if __name__ == "__main__":
    client()
