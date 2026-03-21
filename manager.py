import json
from rich.table import Table
from rich.console import Console
from models import Incident 

class IncidentManager: 
    def __init__(self):
        self.incidents = []
        self.next_id = 1

    def create_incident(self, title, attack_type, severity):
        status = "open"
        incident = Incident(self.next_id, title, attack_type, severity, status)
        self.incidents.append(incident)
        self.next_id += 1
        return incident
    
    def list_incidents(self):
        console = Console()
        table = Table(title="Cybersecurity Incidents")

        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Attack Type", style="green")
        table.add_column("Severity", justify="center", style="red")
        table.add_column("Status", justify="center", style="yellow")

        
        for incident in self.incidents:
            table.add_row(str(incident.incident_id), 
                              incident.title, 
                              incident.attack_type,
                              incident.severity, 
                              incident.status
                        )

        console.print(table)
       
    def update_status(self, incident_id, new_status): 
        for incident in self.incidents: 
            if incident.incident_id == incident_id: 
                incident.status = new_status
                return True
        return False
    
    def delete_incident(self, incident_id):
        for incident in self.incidents:
            if incident.incident_id == incident_id:
                self.incidents.remove(incident)
                return True
        return False
    
    def search_incidents(self, keyword=None, severity=None):
        results = []
        for incident in self.incidents:
            title_match = True 
            severity_match = True

            if keyword:
                title_match = keyword.lower() in incident.title.lower()
            if severity: 
                severity_match = severity.lower() == incident.severity.lower()
            if title_match and severity_match:
                results.append(incident)
        return results
    
    def display_incidents(self, incidents): 
        console = Console()
        table = Table(title="Search Results")
        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Title", justify="center", style="magenta")
        table.add_column("Attack Type", justify="center", style="green")
        table.add_column("Severity", justify="center", style="red")
        table.add_column("Status", justify="center", style="yellow")
        for incident in incidents:
            table.add_row(str(incident.incident_id), 
                              incident.title, 
                              incident.attack_type,
                              incident.severity, 
                              incident.status
                        )
        console.print(table)

    def save_file(self, filename="incidents.json"):
        data = []
        for incident in self.incidents:
            data.append({
                "incident_id": incident.incident_id,
                "title": incident.title,
                "attack_type": incident.attack_type,
                "severity": incident.severity,
                "status": incident.status
            })
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        
    def load_file(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                
                for item in data:
                    incident = Incident(
                        item["incident_id"],
                        item["title"],
                        item["attack_type"],
                        item["severity"],
                        item["status"]
                    )
                    self.incidents.append(incident)
                if data:
                    self.next_id = max(item["incident_id"] for item in data) + 1
                
        except FileNotFoundError:
            print("No file found.")
            pass

    def generate_report(self): 
        report ={
            "High": 0, "Medium": 0, "Low": 0
             }

        for incident in self.incidents: 
            sev = incident.severity.capitalize()
            if sev in report: 
                report[sev] += 1
        return report
    
    def display_report(self, report): 
        console = Console()
        table = Table(title="Incident Severity Report")
        table.add_column("Severity", justify="center", style="red")
        table.add_column("Count", justify="center", style="cyan")
        report = self.generate_report()
        for severity, count in report.items():
            table.add_row(severity, str(count))
        console.print(table)