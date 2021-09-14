import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/recup_pion/"

class RequetePion:
    def recup_pion(choix):
        dict = {"choix": choix}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + choix, json=dict,
                                headers=header)
        return json.loads(requete.text)

    def recup_pion1(choix):
        dict = {"choix": choix}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + choix, json=dict,
                                headers=header)
        return json.loads(requete.text)