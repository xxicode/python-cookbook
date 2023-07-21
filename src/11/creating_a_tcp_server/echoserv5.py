# Echo server using sockets directly

from socket import socket, AF_INET, SOCK_STREAM

def echo_handler(address, client_sock):
    print(f'Got connection from {address}')
    while True:
        if msg := client_sock.recv(8192):
            client_sock.sendall(msg)
        else:
            break
    client_sock.close()

def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)

if __name__ == '__main__':
    echo_server(('', 20000))
