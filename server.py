import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 6380         # same port Redis uses

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    with conn:
        while True:
            data = conn.recv(1024)  # receive up to 1024 bytes
            if not data:
                break               # client disconnected
            print(f"Received: {data}")
            conn.sendall(b"+PONG\r\n")  # send back a response

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()  # wait for a connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()               # handle each client in a new thread

start_server()
