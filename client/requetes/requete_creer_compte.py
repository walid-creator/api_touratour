from lxml import etree
import requests
import json

from serveur.service.configuration import properties

#indique au serveur que les données sont sous la forme d'un JSON
header = {"charset": "utf8"}
RESOURCE_joueurs_PATH = "/joueurs"

class RequeteCreerCompte:

    @staticmethod
    def TesterPseudo(pseudo):
        """
        Envoie le pseudo au web service pour l'ajouter en base
        :param pseudo: le pseudo à ajouer
        :type pseudo: str
        :return: Si l'insertion s'est bien passée
        :rtype: bool
        """
        #Creation du dictionnaire
        dict = {"pseudo": pseudo}     
        requete = requests.post(properties.host_ws + RESOURCE_joueurs_PATH + "/tester_pseudo/" + pseudo, json = dict, headers = header)
        res_requete = 3
        if requete.status_code == 402:
            res_requete = 1
        elif requete.status_code == 200:
            res_requete = 2
        elif requete.status_code == 401:
            res_requete = 0
        else:
            res_requete = 3
        return res_requete
        

    def CreerCompte(pseudo, mdp):
        """
        Envoie les informations sur le joueur au web service pour l'ajouter en base
        :param mdp: le mdp à tester
        :type mdp: string
        :return: Si l'insertion s'est bien passée
        :rtype: 0,1 ou 2
        """
        #Creation du dictionnaire
        dict = {"pseudo": pseudo, "mdp": mdp}
        requete = requests.post(properties.host_ws + RESOURCE_joueurs_PATH + "/creer_joueur/" + pseudo, json = dict, headers = header)
        if requete.status_code == 200:
            res = 1
        elif requete.status_code == 401:
            res = 0
        else:
            res = 2
        return res

