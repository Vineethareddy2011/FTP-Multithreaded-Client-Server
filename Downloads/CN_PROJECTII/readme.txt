Problem:
Implementation of file transfer application for client and server with multiple threads

1.First start the server file 
-> commands: python server.py 
-> give the port number 

2.Client 1 setup: 
-> run the client file
-> commands: python client.py

3.Client 2 setup:  
-> run the client file
-> commands: python client.py

4.The commands given at client side :
-> get <file_name> -> to download a file from the server
-> upload <file_name> -> to upload a file to the server
-> exit -> to close the server connection.


Test Cases:
-> Start the server.
-> Start the client.
-> Use the command python client.py <port_number> in one terminal to connect the first client.
-> Use the command  python client.py <port_number> in another terminal to connect the second client.
-> Try commands like get <filename>, upload <filename>, and exit simultaneously on both clients.
-> Attempt to download a file that is not available on the server to receive an error message.
-> Try uploading a file from the client that does not exist to receive an error message.
-> Enter an invalid command on the client to receive an error message.
-> Typing exit will close the connection with the server.