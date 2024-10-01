from scapy.all import IP, TCP, sr1
from concurrent.futures import ThreadPoolExecutor

class SYNScan:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    def scan_port(self, port):
        try:
            syn_packet = IP(dst=self.target_ip) / TCP(dport=port, flags="S")
            response = sr1(syn_packet, timeout=0.5, verbose=0)
            if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                return port
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
