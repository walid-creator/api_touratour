import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/1000Bornes"

class RequeteGetStatut:
    
    def get_all_statuts(partie):
        dict = {"partie": partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/statuts/" + partie, json=dict, headers = header)
        return json.loads(requete.text)
