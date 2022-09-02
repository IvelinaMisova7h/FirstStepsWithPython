import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
my_socket.send(command)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
my_socket.close()
