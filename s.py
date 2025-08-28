import socket
from datetime import datetime

host = "127.0.0.1"
port = 7272

with socket.socket(socket.AF_INET,) as s:
    s.bind((host, port))
    s.listen(5)
    print(f"Server is listening on {host}:{port}...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        connect_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode()
        conn.sendall(connect_time)