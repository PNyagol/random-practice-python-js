import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
server_host = '127.0.0.1'  # localhost
server_port = 8081

# Connect to the server
client_socket.connect((server_host, server_port))

# Receive data from the server
time_data = client_socket.recv(1024)  # Max 1024 bytes
print("Current time from server:", time_data.decode())

# Close the connection
client_socket.close()