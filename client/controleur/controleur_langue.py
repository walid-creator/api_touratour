from client.requetes.requete_langue import RequeteLangue


class ControleurLangue:

    def recup_langue(choix):
        response_json = RequeteLangue.recup_langue(choix)
        for i in range(len(response_json)):
            return response_json[i][0]