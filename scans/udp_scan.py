import socket
from concurrent.futures import ThreadPoolExecutor

class UDPScan:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(b"", (self.target_ip, port))

            try:
                data, _ = sock.recvfrom(1024)
                print(f"Port {port} is open or responding")
                return port
            except socket.timeout:
                print(f"Port {port} is open or filtered (no response)")
                return port
            except Exception as e:
                print(f"Error receiving data from port {port}: {e}")

        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            sock.close()

    def run(self):
        open_ports = []
        print(f"Starting UDP scan on {self.target_ip} from port {self.start_port} to {self.end_port}")

        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(self.scan_port, port) for port in range(self.start_port, self.end_port + 1)]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
                    print(f"Port {result} is open or filtered")
                    
        return open_ports
