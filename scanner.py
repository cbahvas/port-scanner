# Educational use only , only scan hosts you own or have explicit permission to scan.

import socket

def scan_port(host, port, timeout=0.3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def scan_range(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port}: OPEN")

if __name__ == "__main__":
    scan_range("127.0.0.1", 1, 1024)