print("Incident class started")

class Incident:
    def __init__(self,incidentid,title,attacktype,severity,status): 
        self.incidentid = incidentid
        self.title = title
        self.attacktype = attacktype
        self.severity = severity
        self.status = status

    def display(self):
        print(f"Incident ID: {self.incidentid}")
        print(f"Title: {self.title}")
        print(f"Attack Type: {self.attacktype}")
        print(f"Severity: {self.severity}")
        print(f"Status: {self.status}")
        