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
    