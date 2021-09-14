from client.requetes.requete_get import RequeteGet
import requests
import json
from serveur.service.configuration import properties

header = {"charset":"utf8"}

class RequeteGrille:
    def modifier(id_partie, numcase, valeur):

        # Creation du dictionnaire
        dict = {"id_partie":id_partie, "numcase": numcase, "valeur": valeur}
        requete = requests.post(properties.host_ws + "/jeux/" + "morpion/" + "modification/"+ str(id_partie)+"/"+ str(numcase)+"/"+ str(valeur), json=dict, headers=header)
        if requete.status_code == 200:
            return True
        else:
            return False

    def recuperer(id_partie,nb_cases):
        chemin = "/jeux/"
        dict = {"id_partie": id_partie, "nb_cases":nb_cases}
        requete = requests.post(properties.host_ws + chemin + "morpion/recuperation_grille/"+ str(id_partie), json=dict, headers=header)
        return json.loads(requete.text)


    def pleine(id_partie):
       
       chemin = "/jeux/"
       dict = {"id_partie": id_partie}
       requete = requests.post(properties.host_ws + chemin+ "morpion/grille/pleine/"+str(id_partie), json=dict, headers=header)
       if requete.status_code == 200:
           return True
       else:
           return False

   
    def alignergrille(id_partie, pion):
        chemin = "/jeux/"
        dict = {"id_partie": id_partie, "pion": pion}
        requete = requests.post(properties.host_ws + chemin+ "morpion/grille/aligne/"+str(id_partie)+"/"+str(pion), json=dict, headers=header)
        if requete.status_code == 200:
           return True
        else:
            return False

    def verif_case_pleine(id_partie, numcase):
        chemin = "/jeux/"
        dict = {"id_partie": id_partie, "numcase": numcase}
        requete = requests.post(properties.host_ws + chemin+ "morpion/grille/verif_case/"+str(id_partie)+"/"+str(numcase), json=dict, headers=header)
        if requete.status_code == 200:
           return True
        else:
            return False
