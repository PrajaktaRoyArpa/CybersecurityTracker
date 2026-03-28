import json
import os
from rich.table import Table
from rich.console import Console
from rich.rule import Rule
from models import Incident



class Storage:
    
    def __init__(self, filename="incidents.json"):
        self.filename = filename

    def save(self, incidents):
        data = []
        for incident in incidents:
            data.append({
                "incident_id": incident.incident_id,
                "title": incident.title,
                "attack_type": incident.attack_type,
                "severity": incident.severity,
                "status": incident.status,
                "date": incident.date
            })
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: data file has been corrupted. Starting fresh.")
            return []


class IncidentManager:

    valid_severities = ["Low", "Medium", "High"]
    valid_statuses   = ["Open", "Resolved", "Closed"]

    def __init__(self):
        self.incidents = []
        self.next_id = 1
        self.storage = Storage()

    def create_incident(self, title, attack_type, severity):
    
        if severity.capitalize() not in self.valid_severities:
            print(f"Invalid severity. Choose from: {', '.join(self.valid_severities)}")
            return None
        status = "Open"
        incident = Incident(self.next_id, title, attack_type, severity.capitalize(), status)
        self.incidents.append(incident)
        self.next_id += 1
        self.storage.save(self.incidents)  
        return incident

    def list_incidents(self):
        console = Console()
        if not self.incidents:
            console.print("[yellow]No incidents found.[/yellow]")
            return
        table = Table(title="Cybersecurity Incidents")
        table.add_column("ID",justify="center", style="cyan",no_wrap=True)
        table.add_column("Title",style="magenta")
        table.add_column("Attack Type",style="green")
        table.add_column("Severity", justify="center", style="red")
        table.add_column("Status",justify="center", style="yellow")
        table.add_column("Date",justify="center", style="dim")
        for incident in self.incidents:
            table.add_row(
                str(incident.incident_id),
                incident.title,
                incident.attack_type,
                incident.severity,
                incident.status,
                incident.date
            )
        console.print(table)

    def update_status(self, incident_id, new_status):
        if new_status.capitalize() not in self.valid_statuses:
            print(f"Invalid status. Choose from: {', '.join(self.valid_statuses)}")
            return False
        for incident in self.incidents:
            if int(incident.incident_id) == int(incident_id):
                incident.status = new_status.capitalize()
                self.storage.save(self.incidents)  
                return True
        return False

    def delete_incident(self, incident_id):
        for incident in self.incidents:
            if int(incident.incident_id) == int(incident_id):
                self.incidents.remove(incident)
                self.storage.save(self.incidents)  
                return True
        return False

    def search_incidents(self, keyword=None, severity=None):
        results = []
        for incident in self.incidents:
            title_match    = True
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
        if not incidents:
            console.print("[yellow]No matching incidents found.[/yellow]")
            return
        table = Table(title="Search Results")
        table.add_column("ID",justify="center", style="cyan",no_wrap=True)
        table.add_column("Title",justify="center", style="magenta")
        table.add_column("Attack Type",justify="center", style="green")
        table.add_column("Severity",justify="center", style="red")
        table.add_column("Status", justify="center", style="yellow")
        table.add_column("Date",justify="center", style="dim")
        for incident in incidents:
            table.add_row(
                str(incident.incident_id),
                incident.title,
                incident.attack_type,
                incident.severity,
                incident.status,
                incident.date
            )
        console.print(table)

    def load_file(self):
        data = self.storage.load()
        for item in data:
            incident = Incident(
                int(item["incident_id"]),
                item["title"],
                item["attack_type"],
                item["severity"],
                item["status"],
                item.get("date")
            )
            self.incidents.append(incident)
        if data:
            self.next_id = max(int(item["incident_id"]) for item in data) + 1

    def save_file(self):
        self.storage.save(self.incidents)

    def generate_report(self):
        report = {"High": 0, "Medium": 0, "Low": 0}
        for incident in self.incidents:
            sev = incident.severity.capitalize()
            if sev in report:
                report[sev] += 1
        return report

    def display_report(self, report):
        console = Console()
        console.print(Rule("[bold red]Incident Severity Report[/bold red]"))
        table = Table()
        table.add_column("Severity", justify="center", style="red")
        table.add_column("Count",    justify="center", style="cyan")
        total = sum(report.values())
        for severity, count in report.items():
            table.add_row(severity, str(count))
        table.add_row("[bold]TOTAL[/bold]", f"[bold]{total}[/bold]")
        console.print(table)