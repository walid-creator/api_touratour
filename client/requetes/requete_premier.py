import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/recup_premier/"

class RequetePremier:
    def recup_premier(choix):
        dict = {"choix": choix}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + choix, json=dict,
                                headers=header)
        return json.loads(requete.text)