

import requests
from serveur.service.configuration import properties
import json

RESOURCE_PATH = properties.url_statistiques
class RequeteClassement:
    def __init__(self, chemins):
        self.RESOURCE_PATH = chemins  # "/..."
    @staticmethod
    def getallMorpion(self):

        requete = requests.get(properties.host_ws + self.RESOURCE_PATH)
        return json.loads(requete.text)

    @staticmethod
    def getall1000B(self):

        requete = requests.get(properties.host_ws + self.RESOURCE_PATH)
        return json.loads(requete.text)
