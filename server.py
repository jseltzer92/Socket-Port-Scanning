import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 65432

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(b"Message received")

        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Server shut down.")

if __name__== "__main__":
    start_server()

    