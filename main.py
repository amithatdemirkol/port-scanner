import argparse
from scans.tcp_scan import TCPScan
from scans.udp_scan import UDPScan
from scans.syn_scan import SYNScan
from vulnerabilities.vulnerability_checker import VulnerabilityChecker
from reports.json_report import JSONReport
from reports.html_report import HTMLReport

def parse_arguments():
    parser = argparse.ArgumentParser(description="Comprehensive port and vulnerability scanner")
    parser.add_argument("target", help="Target IP address to scan")
    parser.add_argument("--start-port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end-port", type=int, default=65535, help="End port (default: 65535)")
    parser.add_argument("--scan-type", choices=["tcp", "udp", "syn"], default="tcp", help="Type of scan (default: tcp)")
    parser.add_argument("--report-type", choices=["json", "html"], default="json", help="Type of report (default: json)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    target_ip = args.target
    start_port = args.start_port
    end_port = args.end_port
    scan_type = args.scan_type
    report_type = args.report_type

    if scan_type == "tcp":
        scanner = TCPScan(target_ip, start_port, end_port)
    elif scan_type == "udp":
        scanner = UDPScan(target_ip, start_port, end_port)
    else:
        scanner = SYNScan(target_ip, start_port, end_port)

    open_ports = scanner.run()

    vuln_checker = VulnerabilityChecker(open_ports)
    vuln_checker.check_vulnerabilities()

    if report_type == "json":
        report = JSONReport(open_ports)
    else:
        report = HTMLReport(open_ports)
    
    report.generate_report()
