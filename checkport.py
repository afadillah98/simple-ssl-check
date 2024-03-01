import socket

def check_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Set timeout to 2 seconds

        # Attempt to connect to the host and port
        s.connect((host, port))
        print(f"Port {port} is open on {host}")
        s.close()
    except socket.error:
        print(f"Port {port} is closed on {host}")

if __name__ == "__main__":
    host = "sib.seal.or.id"  # Change to the host you want to check
    port = 80  # Change to the port you want to check
    check_port(host, port)
