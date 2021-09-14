from client.requetes.requete_get_parties import RequeteGetParties
# from serveur.service.configuration import properties

class ControleurPartie :
    def demander_partiesM(jeu):
        response_json = RequeteGetParties.demander_partiesM(jeu)
        lan=[]
        for t in range(len(response_json)):
            if int(response_json[t][6])==1:
                lan.append("Français")
            elif int(response_json[t][6])==2:
                lan.append("Espagnol")
            elif int(response_json[t][6])==3:
                lan.append("Italien")
            elif int(response_json[t][6])==4:
                lan.append("Anglais")
            elif int(response_json[t][6])==5:
                lan.append("Lituanien")
            elif int(response_json[t][6])==6:
                lan.append("Néerlandais")

        print("Parties en attente de joueurs pour le jeu : " + str(jeu))

        tab = [['', '', '', ''], ['id_partie', 'Nombre de joueurs nécessaire', 'Nombre de places restantes', 'Langue'],
               ['', '', '', '']]
        for index in range(len(response_json)):
            tab.append([str(response_json[index][0]), str(response_json[index][3]), str(int(response_json[index][3]) - int(response_json[index][5])), lan[index]])
        form = "{0:14}{1:37}{2:32}{3:23}"
        for val in tab:
            print(form.format(*val))

    def demander_parties(jeu):
        response_json = RequeteGetParties.demander_parties(jeu)
        print("Parties en attente de joueurs pour le jeu : " + str(jeu))

        tab = [['', '', ''], ['id_partie', 'Nombre de joueurs nécessaire', 'Nombre de places restantes'],
               ['', '', '']]
        for index in range(len(response_json)):
            tab.append([str(response_json[index][0]), str(response_json[index][3]), str(int(response_json[index][3]) - int(response_json[index][5]))])
        form = "{0:14}{1:37}{2:23}"
        for val in tab:
            print(form.format(*val))

    def choisir_partie(id_partie, jeu, pseudo):
        req = RequeteGetParties.choisir_partie(id_partie, jeu, pseudo)
        if req == True:
            return True
        else :
            return False

    def creer_partie(jeu, pseudo, param):
        response_json = RequeteGetParties.creer_partie(jeu, pseudo, param)
        return response_json

    def get_Participants(id_partie):
        response_json = RequeteGetParties.get_participants(id_partie)
        tab = []
        for i in range(len(response_json)):
            tab.append([str(response_json[i][0])])
        return tab

    def get_Param(id_partie):
        response_json = RequeteGetParties.get_param(id_partie)
        tab = response_json[0][1]
        return tab

