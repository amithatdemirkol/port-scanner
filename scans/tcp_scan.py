import socket
from concurrent.futures import ThreadPoolExecutor

class TCPScan:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.target_ip, port))
            if result == 0:
                return port
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    def run(self):
        open_ports = []
        with ThreadPoolExecutor(max_workers=500) as executor:
            futures = [executor.submit(self.scan_port, port) for port in range(self.start_port, self.end_port + 1)]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
                    print(f"Port {result} is open")
        return open_ports
