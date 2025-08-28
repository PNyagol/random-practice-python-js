import socket
from datetime import datetime

host = "127.0.0.1"
port = 9797

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    data = s.recv(1024)
    print(f"Receiving from server: {data.decode("utf-8")}")