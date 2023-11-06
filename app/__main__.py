import socket
import threading
from os import environ


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 0))
    _, port = sock.getsockname()
    return sock, port


def enable_to_listener(sock, port):
    sock.listen(1)
    print(f'📭 Socket listener on port {port}')
    return sock, port


def connection_receiver(sock, port):
    t = threading.Thread(target=accept_connections, args=(sock, port))
    t.start()


def accept_connections(sock, port):
    while True:
        _, client_addr = sock.accept()
        print(f'📬 Port {port} receiving connection from: {client_addr=}')


if __name__ == '__main__':
    num_sockets = int(environ.get('NUM_SOCKETS', 1))

    sockets = [create_socket() for _ in range(num_sockets)]
    enabled_listener = [enable_to_listener(*sock) for sock in sockets]
    [connection_receiver(*sock) for sock in sockets]

    print(
        'To access exposed ports, you can try:\n',
        f'\ttelnet {socket.gethostbyname(socket.gethostname())} PORT',
    )
