import socket

host = "127.0.0.1"
port = 9797

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    name = input("Enter name: ")
    s.send(name.encode("utf-8"))  # send name first
    
    data = s.recv(1024)  # then wait for server's reply
    print(f"Receiving from server: {data.decode('utf-8')}")
