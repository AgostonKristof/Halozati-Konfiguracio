import socket
def check_dns(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"{domain_name} IP-címe: {ip_address}")
    except socket.gaierror:
        print(f"{domain_name} nem érhető el vagy helytelen a domain név.")
check_dns('google.com')