# Educational use only , only scan hosts you own or have explicit permission to scan.

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout=0.3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def scan_range(host, start_port, end_port, timeout=1, max_workers=100):
    ports = range(start_port, end_port +1)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(lambda port: (port, scan_port(host, port, timeout)), ports)

    for port, is_open in results:
        if is_open:
            print(f"Port {port}: OPEN")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("host", help="Target host to scan (IP or hostname)")
    parser.add_argument("--start-port", type=int, default=1, help="First port to scan (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="Last port to scan (default: 1024)")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout per port in seconds (default: 1.0)")
    args = parser.parse_args()

    scan_range(args.host, args.start_port, args.end_port, args.timeout)