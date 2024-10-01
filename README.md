# Port Scanning and Vulnerability Scanning Tool

This project is a modular and high-performance Port Scanning and Vulnerability Scanning tool, designed to scan all ports on a target system. It supports TCP, UDP, and SYN scans and provides a framework for checking for potential vulnerabilities based on the detected open ports and services. The project is optimized for speed, utilizing multi-threading and other performance enhancements, and is built with a clean and modular architecture.

## Features of the project
- **TCP Scanning**: Detects open TCP ports on the target.
- **UDP Scanning**: Discovers open or filtered UDP ports.
- **SYN Scanning**: Performs a SYN scan to detect open ports using SYN-ACK response.
- **Vulnerability Scanning**: Based on open ports and associated services, checks for known vulnerabilities.
- **Command Line Interface (CLI)**: Provides an easy-to-use interface for running scans and viewing results.
- **Highly Modular Structure**: Easy to extend with new scanning techniques or vulnerability checks.


## Installation

### Prerequisites

- **Python 3.1x**
- **Required libraries:**:
    - scapy
    - socket
    - argparse
    - concurrent.futures

 ***Install the necessary dependencies using pip:***
 ```bash
 pip install scapy
```
### For Windows users:
Make sure to install Npcap from Npcap [Npcap](npcap.com)
 to use Scapy for network packet capture. During installation, enable "WinPcap API-compatible mode."


### For Linux/macOS users:
Install **libpcap** by running:

 ```bash
# Ubuntu/Debian
sudo apt-get install libpcap-dev

# macOS (using Homebrew)
brew install libpcap
```
## Usage

You can run the tool from the command line interface (CLI) to perform TCP, UDP, or SYN scans.

### Running TCP Scan:

```bash
python main.py --scan-type tcp --target <TARGET_IP> --start-port <START_PORT> --end-port <END_PORT>
```

### Running UDP Scan:
```bash
python main.py --scan-type udp --target <TARGET_IP> --start-port <START_PORT> --end-port <END_PORT>
```

### Running SYN Scan:
```bash
python main.py --scan-type syn --target <TARGET_IP> --start-port <START_PORT> --end-port <END_PORT>
```

### Full Port Scan Example:
```bash
python main.py --scan-type tcp --target 192.168.1.1 --start-port 1 --end-port 65535
```

### Additional Arguments

- **--scan-type** : Specify the type of scan (tcp, udp, syn).
- **--target** : The target IP address to scan.
- **--start-port** : The start of the port range to scan.
- **--end-port** : The end of the port range to scan.
 
## Contributing

 - Fork the repository.
 - Create your feature branch (git checkout -b feature/my-feature).
 - Commit your changes (git commit -m 'Add my feature').
 - Push to the branch (git push origin feature/my-feature).
 - Open a pull request.

**Developed by 👨‍💻 Ahmet Mithat Demirkol**