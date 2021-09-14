from client.requetes.requete_classement import RequeteClassement
from serveur.service.configuration import properties

# Classes qui affichent le classement des meilleurs joueurs pour les différents jeux 

class ControleurClassement:

    def demander_classement_morpion():
        req = RequeteClassement(properties.url_statistiques + '/Morpion')
        response_json = RequeteClassement.getallMorpion(req)

        print("Classement des 10 meilleurs joueurs du Morpion")

        tab = [['', '', '', '', '', ''], ['Pseudo', '% de parties gagnées ', 'Nb de parties gagnées ', 'Nb de parties jouées '],
               ['', '', '', '', '', '']]
        for index in range(len(response_json)):
            tab.append([str(response_json[index][0]), str(response_json[index][2]), str(response_json[index][1]),str(response_json[index][3])])
        form = "{0:14}{1:27}{2:23}{3:7}"
        for val in tab:
            print(form.format(*val))

    def demander_classement_1000B():
        req = RequeteClassement(properties.url_statistiques + '/1000Bornes')
        response_json = RequeteClassement.getall1000B(req)

        print("Classement des 10 meilleurs joueurs du 1000 Bornes")

        tab = [['', '', '', '', '', ''], ['Pseudo', '% de parties gagnées ', 'Nb de parties gagnées ', 'Nb de parties jouées '],
               ['', '', '', '', '', '']]
        for index in range(len(response_json)):
            tab.append([str(response_json[index][0]), str(response_json[index][2]), str(response_json[index][1]),str(response_json[index][3])])
        form = "{0:14}{1:27}{2:23}{3:7}"
        for val in tab:
            print(form.format(*val))


