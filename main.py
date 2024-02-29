import ssl
import socket
import datetime

def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

            return cert

# Example usage:
hostname = "name_of_the hostname" # Example: "sib.seal.or.id"
# expiry_date = get_ssl_expiry_date(hostname)
# print(f"SSL certificate for {hostname} expires on: {expiry_date}")