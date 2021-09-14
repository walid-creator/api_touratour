from client.requetes.requete_get import RequeteGet
from serveur.service.configuration import properties


class ControleurDemanderListeJeux:

    def demander_liste_jeux():
        req = RequeteGet("/jeux")
        response_json = RequeteGet.getall(req)

        for i in range(len(response_json)):
            print(response_json[i][1])