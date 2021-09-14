import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/parametres"

class RequeteParam:
    def creer_param_m(id_partie,valeur):
        dict = {"id_partie": id_partie, "valeurparam": valeur}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/creer_param/" + id_partie, json=dict,
                                headers=header)
        return json.loads(requete.text)
            
    def recuperer_param(id_participant, nomParam):
        dict = {"id_participant":id_participant ,"nomParam": nomParam}
        requete = requests.post(properties.host_ws + "/jeux/morpion/recup_param/" + str(id_participant)+"/"+str(nomParam), json=dict,headers=header)
        return json.loads(requete.text)        