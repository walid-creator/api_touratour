from client.assets.assets import border

class MenuFinJeu():
    title = 'Que voulez-vous faire ?'
    options = ["Rejouer",
               "Quitter le jeu"]
    nb_options = len(options)

    def run(self):

        print(MenuFinJeu.title)

        for i, mes in enumerate(MenuFinJeu.options):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue
            if choice <= 0 or choice > MenuFinJeu.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                # return On rejoue le jeu donc menu du tour a tour sur la meme partie
                border()

            elif choice == 2:
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
                border()

