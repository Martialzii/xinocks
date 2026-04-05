import socket
from datetime import datetime

class PortWatcher:
    def __init__(self):
        self.target = "127.0.0.1" # Scanning your own machine
        self.common_ports = [21, 22, 80, 443, 8080, 3306]

    def scan(self):
        print(f"--- MARTIALZII PORT AUDIT: {datetime.now().strftime('%H:%M:%S')} ---")
        for port in self.common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((self.target, port))
            status = "OPEN [!]" if result == 0 else "Closed"
            print(f"Port {port}: {status}")
            s.close()

if __name__ == "__main__":
    watcher = PortWatcher()
    watcher.scan()