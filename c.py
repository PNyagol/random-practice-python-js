import socket
from datetime import datetime

host = "127.0.0.1"
port = 7272

with socket.socket(socket.AF_INET,) as s:
    s.connect((host, port))
    data = s.recv(1024)
    print(f"Received from server: {data.decode("utf-8")}")