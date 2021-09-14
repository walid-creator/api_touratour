from client.assets.assets import border
from client.requetes.requete_get_parties import RequeteGetParties


class MenuQuelleCarte():
    title = 'Quelle carte vouez vous jouer?'

    def run(id_participant, id_partie):

        # get la main du joueur on l'appelle MAIN
        main = RequeteGetParties.obtenir_main(id_participant)

        # MAIN = ["carte1","carte2","carte3","carte4","carte5","carte6", "carte7"]
        MAIN = []
        for i in range(int(len(main)/4)):
            MAIN += [main[4*i : 4*i+4]]

        nb_options = len(MAIN)

        # print les statuts
        for i in range(int(RequeteGetParties.get_param(id_partie)[0][1])):
            id_particip = RequeteGetParties.obtenir_id_particip(id_partie, (i + 1))
            print('Le statut de ' + RequeteGetParties.obtenir_pseudo(id_particip) + ' : ')
            print(RequeteGetParties.obtenir_statut(id_particip)[0])

        # print la derniere carte de la poubelle
        carte = [RequeteGetParties.obtenir_derniere_carte_poubelle(id_partie)]
        print('La dernière carte de la poubelle est : ', carte)

        # print la main
        print('Votre main : ', MAIN)

        print(MenuQuelleCarte.title)

        for i, mes in enumerate(MAIN):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue

            if choice <= 0 or choice > nb_options:
                print("Petit blagueur")
                continue

            else:
                border()
                carte_choisie = MAIN[choice - 1]
                # CarteAJouer = carte choisie
                from client.IHM.MenusQuiMarchent.MenuChoixTarget import MenuChoixTarget
                return MenuChoixTarget.run(id_partie, id_participant, carte_choisie)
                border()




