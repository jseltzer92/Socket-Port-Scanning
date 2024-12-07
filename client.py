import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 65432

    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        message = input("Enter a message to send: ")
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Client disconnected.")

if __name__ == "__main__":
    start_client()