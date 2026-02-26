import socket as s


server_ip = "localhost"
server_port = 8080

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

request = "GET /index.html HTTP/1.0\r\n\r\n"
badRequest = "GET /badReq.html HTTP/1.0\r\n\r\n"

#Change to badRequest.encode() to test 404 error
client_socket.send(request.encode())

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(data.decode())

client_socket.close()
