from client.requetes.requetestat import RequeteStat


class ControleurStat:
    def demander_stat(pseudo):
        response_json = RequeteStat.stat_un_joueur(pseudo)
        for i in range(len(response_json)):
            print("Jeu : ", response_json[i][0])
            print("Nb de parties gagnées : ", response_json[i][2])
            print("% de parties gagnées : ", response_json[i][3])
            print("Nombre de parties : ", response_json[i][5])
            print(""
                  "")