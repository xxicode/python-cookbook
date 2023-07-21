from socket import socket, AF_INET, SOCK_STREAM
from auth import server_authenticate

secret_key = b'peekaboo'

def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return
    while True:
        if msg := client_sock.recv(8192):
            client_sock.sendall(msg)
        else:
            break

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c,a = s.accept()
        echo_handler(c)

print('Echo server running on port 18000')

echo_server(('', 18000))
