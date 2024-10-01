class HTMLReport:
    def __init__(self, results):
        self.results = results

    def generate_report(self, filename="scan_report.html"):
        html_content = "<html><head><title>Scan Report</title></head><body><h1>Scan Results</h1><ul>"
        for port, status in self.results.items():
            html_content += f"<li>Port {port}: {status}</li>"
        html_content += "</ul></body></html>"

        with open(filename, 'w') as f:
            f.write(html_content)
        print(f"Report saved as {filename}")

