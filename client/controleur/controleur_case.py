from client.requetes.requete_case import RequeteCase


class ControleurCase:

    def recup_nbcases(id_partie):
        response_json = RequeteCase.recup_nbcases(id_partie)
        for i in range(len(response_json)):
            return response_json[i][0]