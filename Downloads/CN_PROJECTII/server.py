import socket
import threading
import utils

IP = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"

def handle_client(connection, address):
    print(f"New Connection from {address}: Connected.")
    while True:
        try:
            command = connection.recv(1024).decode(FORMAT).split(' ')
            if not command[0]:
                break
            fileName = command[1] if len(command) > 1 else None
            if command[0] == 'get' and fileName:
                utils.sendFile(fileName=fileName, connection=connection, prefix='new')
            elif command[0] == 'upload' and fileName:
                utils.receiveFile(fileName=fileName, connection=connection, prefix='new')
            elif command[0] == 'exit':
                break
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"Error: {e}")
            break
    connection.close()
    print(f"Disconnected {address} successfully.")

def server():
    port = input("Enter the port number to listen: ")
    if int(port) <= 1024:
        print("Port number must be greater than 1024.")
        return

    ADDR = (IP, int(port))
    
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening on port {port}")
    try:
        while True:
            connection, address = server.accept()
            thread = threading.Thread(target=handle_client, args=(connection, address))
            thread.start()
    except KeyboardInterrupt:
        print("Server shutdown.")
    finally:
        server.close()

if __name__ == "__main__":
    server()
