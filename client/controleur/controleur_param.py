from client.requetes.requete_param import RequeteParam

class ControleurParam:
    def creer_paramM(id_partie,valeur):
        response_json = RequeteParam.creer_param_m(id_partie,valeur)
        return response_json