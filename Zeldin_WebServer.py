import socket as s

# Set server IP and port
server_ip = "localhost"
server_port = 8080

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen(1)

while True:
    connection_socket, client_address = server_socket.accept()
    print("Connection Accepted")

    try:
        reqFileName = connection_socket.recv(1024).decode()
        fileName = reqFileName.replace("/", "")
        fileName = fileName.split(" ")
        with open(fileName[1], "r") as file:
            connection_socket.send("HTTP/1.0 200 OK".encode())
            data = file.read(1024)
            while data:
                connection_socket.sendall(data.encode())
                data = file.read(1024)


    except FileNotFoundError:
        error = "HTTP/1.0 404 Not Found"
        connection_socket.send(error.encode())


    connection_socket.close()