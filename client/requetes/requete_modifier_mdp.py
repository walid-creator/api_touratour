import json
from serveur.service.configuration import properties
header = {"charset":"utf8"}
import requests


class RequeteModifierMdp:
    def modifier_mdp(pseudo, nvMdp):
        """
        Envoie les informations sur le joueur au web service pour l'ajouter en base
        :param mdp: le mdp à tester
        :type mdp: string
        :return: Si l'insertion s'est bien passée
        :rtype: 0,1 ou 2
        """
        #Creation du dictionnaire
        dict = {"pseudo": pseudo, "mdp": nvMdp}
        requete = requests.put(properties.host_ws + "/joueurs/" + "modification/" + pseudo, json = dict, headers = header)
        if requete.status_code == 200:
            return True
        else: 
            return False
