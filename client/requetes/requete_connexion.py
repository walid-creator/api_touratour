from lxml import etree
import requests
import json
from serveur.service.configuration import properties
header = {"charset":"utf8"}

RESOURCE_joueurs_PATH= "/joueurs"

class RequeteConnexion:
    
    @staticmethod
    def connexion(pseudo, mdp):
        """
        Envoie les informations d'un utilisateur au web service pour vérifier ses informations en base
        :param pseudo: le pseudo entré par l'utilisateur
        :param mdp: le mdp entré par l'utilisateur
        :type pseudo: str
        :type mdp: str
        :return: si la vérification est bonne
        :rtype: bool
        """
        dict = {"pseudo": pseudo, "mdp": mdp}
        requete = requests.post(properties.host_ws + RESOURCE_joueurs_PATH + "/connexion/" + pseudo, json=dict, headers = header)
        res_requete = False
        if requete.status_code == 200:
            res_requete = True
        else:
            res_requete = False
        return res_requete