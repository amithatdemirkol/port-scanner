import json

class JSONReport:
    def __init__(self, results):
        self.results = results

    def generate_report(self):
        with open("scan_report.json", "w") as f:
            json.dump(self.results, f)
        print("JSON report generated.")
