from models import Incident

class IncidentManager: 
    def __init__(self): 
        self.incidets = []
        self._next_id = 1

    def _generate_id(self): 
        incident_id = self._next_id
        self._next_id += 1
        return incident_id
    