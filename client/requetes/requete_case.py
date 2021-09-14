import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/recup_nbcase/"

class RequeteCase:
    def recup_nbcases(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + id_partie, json=dict,
                                headers=header)
        return json.loads(requete.text)