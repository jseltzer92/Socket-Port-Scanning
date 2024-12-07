import socket

def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                else:
                    print(f"Port {port}: CLOSED")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Enter target host (e.g., localhost or scanme.nmap.org): ")
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        port_scanner(target, start_port, end_port)
    except ValueError:
        print("Invalid port number.")
        