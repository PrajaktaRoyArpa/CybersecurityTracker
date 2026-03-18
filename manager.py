from models import Incident 
class IncidentManager: 
    def __init__(self): 
        self.incidents = []
        self.next_id = 1
    
    def create_incident(self, title, attack_type, severity, status):
        status = "Open"
        incident = Incident(self.next_id, title, attack_type, severity, status)
        self.incidents.append(incident)
        self.next_id += 1
        return incident
    
    def list_incidents(self):
        for incident in self.incidents:
            incident.display()
            print("------------------------------------------------")

       
    