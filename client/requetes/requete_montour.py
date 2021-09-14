import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/modifier_mon_tour/"

class ModifTour:
    def modif_tour(id_participant,tour):
        dict = {"id_participant": id_participant,"tour":tour}
        requete = requests.put(properties.host_ws + RESOURCE_PATH + str(id_participant)+"/"+str(tour), json=dict,
                                headers=header)
        return json.loads(requete.text)