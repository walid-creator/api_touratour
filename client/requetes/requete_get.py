import requests
from serveur.service.configuration import properties
import json


class RequeteGet:

    def __init__(self, chemins):
        self.RESOURCE_PATH= chemins #"/..."

    @staticmethod
    def getall(self):
        """
        Envoie les informations d'un monstre au web service pour l'ajouter en base
        :param monstre: le monstre à ajouer
        :type monstre: Monstre
        :return: Si l'insertion c'est bien passé
        :rtype: bool
        """
        requete = requests.get(properties.host_ws + self.RESOURCE_PATH )
        return json.loads(requete.text)


    def get(chemin): 
        requete = requests.get(properties.host_ws +
                             self.RESOURCE_PATH + chemin )
        return json.loads(requete.text)   
           
       

