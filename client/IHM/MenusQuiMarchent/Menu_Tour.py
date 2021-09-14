from client.assets.assets import border
from client.requetes.requete_get_parties import RequeteGetParties


class MenuTour:
    title = 'A vous de jouer, que voulez vous faire?'
    options = ["Piocher une carte dans la pioche",
               "Prendre la carte du haut de la poubelle"]
    nb_options = len(options)

    def run(id_participant, id_partie):

        print(MenuTour.title)
        # print la derniere carte de la poubelle
        # print les statuts
        # print la main
        for i, mes in enumerate(MenuTour.options):
            print("[{}] {}".format(i + 1, mes))


        while True:

            choice = input('\n saisissez votre réponse : ')

            if RequeteGetParties.obtenir_derniere_carte_poubelle(id_partie) == "" and int(choice) == 2:
                print(""
                      "Pas de carte dans la poubelle, vous piochez une carte")
                choice = 1

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue

            if choice <= 0 or choice > MenuTour.nb_options:
                print("Petit blagueur")
                continue


            elif choice == 1:
                border()
                print("Carte tirée : " + RequeteGetParties.piocher_pioche(id_participant, id_partie))
                from client.IHM.MenusQuiMarchent.menu_quelle_carte import MenuQuelleCarte
                return MenuQuelleCarte.run(id_participant, id_partie)
                border()


            elif choice == 2:
                border()
                carte = RequeteGetParties.piocher_poubelle(id_participant, id_partie)
                print("Carte tirée : " + carte + " à jouer directement")
                # CarteAJouer = carte choisie
                from client.IHM.MenusQuiMarchent.MenuChoixTarget import MenuChoixTarget
                return MenuChoixTarget.run(id_partie, id_participant, carte)
                border()
