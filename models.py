print("Incident class started")

class Incident:
    def __init__(self, incident_id, title, attack_type, severity, status): 
        self.incident_id = incident_id
        self.title = title
        self.attack_type = attack_type
        self.severity = severity
        self.status = status
    
    def display(self): 
        print("ID:", self.incident_id)
        print("Title:", self.title)
        print("Attack Type:", self.attack_type)
        print("Severity:", self.severity)
        print("Status:", self.status)

