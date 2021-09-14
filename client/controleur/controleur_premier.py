from client.requetes.requete_premier import RequetePremier


class ControleurPremier:

    def recup_premier(choix):
        response_json = RequetePremier.recup_premier(choix)
        for i in range(len(response_json)):
            return response_json[i][0]