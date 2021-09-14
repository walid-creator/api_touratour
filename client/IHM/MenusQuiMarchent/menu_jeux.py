from client.assets.assets import border
from client.controleur.controleur_classement import ControleurClassement
from client.IHM.MenusQuiMarchent.menu_rejoindre_partie import MenuRejoindrePartie
from client.IHM.MenusQuiMarchent.menu_choix_parametres import MenuChoixParametres


class MenuJeuxClassement():
    """
        Donne le classement personnel à un jeu.
        :param id_partie,: identifiants de la partie 
        :type id_partie: integer
        :return: donne le classement renvoie au menu des fonctionnalités 
    """
    title = 'Quel classement voulez-vous afficher ?'
    options = ['Morpion',
               '1000 Bornes',
               'Revenir au menu précédent']
    nb_options = len(options)

    def run(self):

        print(MenuJeuxClassement.title)

        for i, mes in enumerate(MenuJeuxClassement.options):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue
            if choice <= 0 or choice > MenuJeuxClassement.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                ControleurClassement.demander_classement_morpion()
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()

            elif choice == 2:
                border()
                ControleurClassement.demander_classement_1000B()
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()

            elif choice == 3:
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
                border()



class MenuJeuxCreate():
    """
        Création d'une partie
        :return: menu choix des paramètres pour le jeu choisi
        """
    title = 'Vous voulez créer une partie ? Quel jeu choisissez-vous ?'
    options = ['Morpion',
               '1000 Bornes',
               'Revenir au menu précédent']
    nb_options = len(options)

    def run(self):

        print(MenuJeuxCreate.title)

        for i, mes in enumerate(MenuJeuxCreate.options):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue
            if choice <= 0 or choice > MenuJeuxCreate.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                return MenuChoixParametres.run(1)
                border()

            elif choice == 2:
                border()
                return MenuChoixParametres.run(2)
                border()

            elif choice == 3:
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
                border()



class MenuJeuxJoin():
    """
        Rejoindre une partie existante.
        return menu de la partie du morpion ou du 1000Bornes
        """
    title = 'Vous voulez rejoindre une partie ? Quel jeu choisissez-vous ?'
    options = ['Morpion',
               '1000 Bornes',
               'Revenir au menu precedent']
    nb_options = len(options)

    def run(self):

        print(MenuJeuxJoin.title)

        for i, mes in enumerate(MenuJeuxJoin.options):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue
            if choice <= 0 or choice > MenuJeuxJoin.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                return MenuRejoindrePartie.runM(1)
                border()

            elif choice == 2:
                border()
                return MenuRejoindrePartie.run(2)
                border()

            elif choice == 3:
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
                border()




