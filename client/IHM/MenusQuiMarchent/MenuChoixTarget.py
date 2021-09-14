from client.assets.assets import border
from client.requetes.requete_get_parties import RequeteGetParties
from client.IHM.MenusQuiMarchent.menu_att_tour import MenuAttTour


class MenuChoixTarget:
    title = 'Où voulez vous placer votre carte ? (identifiant de la cible)'

    def run(id_partie, id_participant, carte):

        # Joueurs = [liste des id + poubelle]

        joueurs = []
        I = [0]
        for i in range(int(RequeteGetParties.get_param(id_partie)[0][1])):
            a = RequeteGetParties.obtenir_id_particip(id_partie, (i + 1))
            b = RequeteGetParties.obtenir_pseudo(a)
            joueurs += [[int(a),b]]
            I += [int(a)]

        joueurs += [[0,"Poubelle"]]

        print(MenuChoixTarget.title)
        # print la derniere carte de la poubelle
        # print les statuts
        # print la main

        nb_options = len(joueurs)

        for i in range(nb_options):
            print("[{}] {}".format(joueurs[i][0], joueurs[i][1]))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue

            if choice not in I:
                print("Petit blagueur")
                continue

            else:
                border()
                target = choice
                req = RequeteGetParties.jouer_tour(id_partie, id_participant, carte, target)
                if req == 1:
                    return MenuAttTour.run(id_participant, id_partie)
                if req == 0:
                    print("Bravo, vous avez gagné la partie !")
                    from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                    return MenuFonctionnalites()
                border()





