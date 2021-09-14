from client.requetes.requete_pion import RequetePion

class ControleurPion:

    def recup_pion(choix):
        response_json = RequetePion.recup_pion(choix)
        for i in range(len(response_json)):
            return response_json[i][0]


    def recup_pion1(choix):
        response_json = RequetePion.recup_pion1(choix)
        for i in range(len(response_json)):
            return response_json[i][0]