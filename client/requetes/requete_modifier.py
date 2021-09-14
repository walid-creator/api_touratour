import requests

from configuration import properties


class RequeteModifier:
    def __init__(self,modif):
        self.header = {'Content-Type': 'application/json',"charset":"utf8"}
        self.RESOURCE_PATH = modif 
        
    def nouvelleTache(nom,detail):
        r = requests.post(properties.host_ws+self.RESOURCE_PATH)
        data = json.dumps({"nom":nom,"details":detail}),
        headers = header
        return json.loads(r.text)
        
