import requests
import json
from serveur.service.configuration import properties

header = {"charset":"utf8"}
RESOURCE_stat_PATH = "/statistiques/"

class RequeteStat:


    def stat_un_joueur(pseudo):
        dict = {"pseudo": pseudo}
        requete = requests.post(properties.host_ws + RESOURCE_stat_PATH +  pseudo, json=dict, headers = header)
        return json.loads(requete.text)
