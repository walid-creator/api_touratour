import requests
from serveur.service.configuration import properties
import json

header = {"charset":"utf8"}
RESOURCE_PATH = "/parties"


class RequeteGetParties:
    def demander_partiesM(jeu):
        jeu = str(jeu)
        dict = {"jeu": jeu}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/en_attenteM/" + jeu, json=dict, headers=header)
        return json.loads(requete.text)

    def demander_parties(jeu):
        jeu = str(jeu)
        dict = {"jeu": jeu}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/en_attente/" + jeu, json=dict, headers = header)
        return json.loads(requete.text)

    def choisir_partie(id_partie, jeu, pseudo):
        dict = {"id_partie": id_partie, "jeu": jeu, "pseudo": pseudo}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/rejoindre/" + pseudo, json=dict, headers = header)
        if requete.status_code == 200:
            return True
        else:
            return False

    def creer_partie(jeu, pseudo, param):
        dict = {"id_jeu": jeu, "pseudo": pseudo, "parampartie": param}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/creer_partie/" + pseudo, json=dict, headers=header)
        return json.loads(requete.text)


    def get_participants(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/participants/" + id_partie, json=dict, headers=header)
        return json.loads(requete.text)


    def get_param(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/param/" + str(id_partie), json=dict, headers=header)
        return json.loads(requete.text)


    def donner_ordre(id_partie, nvordre, pseudo):
        dict = {"id_partie": id_partie, "nvordre": str(nvordre), "pseudo": str(pseudo)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/ordre/" + str(id_partie) + "/" + str(pseudo), json=dict, headers=header)
        if requete.status_code == 200:
            return True
        else:
            return False

    def get_id_participant(id_partie, pseudo):
        dict = {"id_partie": id_partie, "pseudo": pseudo}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/get_id_participant/" + id_partie + "/" + pseudo, json=dict, headers=header)
        return json.loads(requete.text)

    def create_pioche(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/creer_pioche/" + id_partie, json=dict, headers=header)
        if requete.status_code == 200:
            return True
        else:
            return False

    def create_poubelle(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/creer_poubelle/" + id_partie , json=dict, headers=header)
        if requete.status_code == 200:
            return True
        else:
            return False

    def get_all_id_participant(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/get_all_id_participant/" + id_partie, json=dict, headers=header)
        return json.loads(requete.text)


    def creer_main(id_participant):
        dict = {"id_participant": str(id_participant)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/creer_main/" + str(id_participant), json=dict,
                                headers=header)
        if requete.status_code == 200:
            return True
        else:
            return False


    def piocher_pioche(id_participant, id_partie):
        dict = {"id_participant": str(id_participant), "id_partie": str(id_partie)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/piocher_pioche/" + str(id_participant) + "/" + str(id_partie), json=dict,
                                headers=header)
        return json.loads(requete.text)


    def creer_statut(id_participant):
        dict = {"id_participant": str(id_participant)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/creer_statut/" + str(id_participant), json=dict,
                                headers=header)
        if requete.status_code == 200:
            return True
        else:
            return False




    def obtenir_id_particip(id_partie, ordre):
        dict = {"id_partie": id_partie, "ordre": ordre}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_id_particip/" + str(id_partie) + "/" + str(ordre), json=dict,
                                headers=header)
        return json.loads(requete.text)

    def obtenir_pseudo(id_particip):
        dict = {"id_participant": id_particip}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_pseudo/" + str(id_particip),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)

    def obtenir_statut(id_particip):
        dict = {"id_participant": id_particip}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_statut/" + str(id_particip),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)

    def obtenir_derniere_carte_poubelle(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_derniere_carte_poubelle/" + str(id_partie),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)

    def obtenir_main(id_participant):
        dict = {"id_participant": id_participant}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_main/" + str(id_participant),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)

    def obtenir_sontour(id_participant):
        dict = {"id_participant": id_participant}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_sontour/" + str(id_participant),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)


    def obtenir_sontour_morpion(id_participant):
        dict = {"id_participant": id_participant}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_sontour/" + str(id_participant),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)    


    def piocher_poubelle(id_participant, id_partie):
        dict = {"id_participant": str(id_participant), "id_partie": str(id_partie)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/piocher_poubelle/" + str(id_participant) + "/" + str(id_partie), json=dict,
                                headers=header)
        return json.loads(requete.text)



    def jouer_tour(id_partie, id_participant, carte, target):
        dict = {"id_participant": str(id_participant), "id_partie": str(id_partie), "carte": str(carte), "target": str(target)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/jouer_tour/" + str(id_participant) + "/" + str(id_partie) + "/" + str(carte) + "/" + str(target), json=dict, headers=header)
        if requete.status_code == 200:
            return 1
        elif requete.status_code == 201:
            return 0
        else:
            return 2

    def obtenir_statutfin(id_partie):
        dict = {"id_partie": str(id_partie)}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_statutfin/" + str(id_partie) , json=dict, headers=header)
        if requete.status_code == 200:
            return 2
        else:
            return 1



    def obtenir_numtour(id_partie):
        dict = {"id_partie": id_partie}
        requete = requests.post(properties.host_ws + RESOURCE_PATH + "/obtenir_numtour/" + str(id_partie),
                                json=dict,
                                headers=header)
        return json.loads(requete.text)
