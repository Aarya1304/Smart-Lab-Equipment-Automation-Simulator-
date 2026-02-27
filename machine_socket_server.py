import socket

# Localhost configuration
HOST = '127.0.0.1'
PORT = 65432

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to host and port
server.bind((HOST, PORT))

# Start listening for incoming connections
server.listen()

print("Machine Simulator Running... Waiting for commands.")

while True:
    # Accept connection from client (Flask API)
    conn, addr = server.accept()

    with conn:
        print("Connected by:", addr)

        # Receive command from client
        data = conn.recv(1024)

        if not data:
            break

        command = data.decode()
        print("Command received:", command)

        # Simulate machine acknowledgment
        response = f"ACK: {command}"

        # Send acknowledgment back to API
        conn.sendall(response.encode())