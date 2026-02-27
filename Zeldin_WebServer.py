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

        # Partitions the file by replacing all / with empty characters and then 
        # splits the string anywhere there is a space, therefore separating the file
        # name from everything else
        fileName = reqFileName.replace("/", "")
        fileName = fileName.split(" ")

        # Reads the file name array's second element because that is where the file
        # name would be after the partitioning
        with open(fileName[1], "r") as file:
            # Sends the 200 OK message
            connection_socket.send("HTTP/1.0 200 OK".encode())

            # Reads the data and sends it to the client to bee printed out
            data = file.read(1024)
            while data:
                connection_socket.sendall(data.encode())
                data = file.read(1024)

    # If file isn't found it will send the error 404 message
    except FileNotFoundError:
        error = "HTTP/1.0 404 Not Found"
        connection_socket.send(error.encode())


    connection_socket.close()
