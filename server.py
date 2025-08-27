import socket
from datetime import datetime

# create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a sspecific object
port = 8081
host = "127.0.0.1"
server_socket.bind((host, port))

# Listen for incoming connections (max 5 queued)
server_socket.listen(5)
print(f"Daytime server listens on {host}:{port}...")

while True:
    # accept connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Get current time and send it
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_socket.send(current_time.encode())

    # close connection
    client_socket.close