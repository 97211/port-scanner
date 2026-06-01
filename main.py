import socket
import sys
from datetime import datetime

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()
    except:
        pass

def main():
    print("=== Simple Port Scanner ===")
    target = input("Enter target IP/domain: ")
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid hostname")
        sys.exit()

    print(f"Scanning {target_ip}")
    print(f"Started at: {datetime.now()}")
    
    try:
        for port in range(1, 1025):
            scan_port(target_ip, port)
    except KeyboardInterrupt:
        print("\nScan stopped by user")
        sys.exit()
    
    print(f"Scan completed at: {datetime.now()}")

if __name__ == "__main__":
    main()
