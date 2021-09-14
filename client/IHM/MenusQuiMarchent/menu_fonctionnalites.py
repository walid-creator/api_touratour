from client.controleur.controleurstat import ControleurStat
from client.IHM.MenusQuiMarchent.menu_jeux import MenuJeuxCreate, MenuJeuxJoin, MenuJeuxClassement
from client.IHM.MenusQuiMarchent.menu_etes_vous_sur import MenuEtesVousSur
from client.assets.assets import border
from client.controleur.controleur_demander_liste_jeux import ControleurDemanderListeJeux
from client.IHM.session import Session
from client.IHM.MenusQuiMarchent.menu_modifier_mdp import MenuModifierMdp

class MenuFonctionnalites():

    title2 = 'Quelle fonctionnalité choisissez-vous ?'
    options = ['Demander la liste des jeux',
               'Créer une partie',
               'Rejoindre une partie',
               'Demander son niveau personnel',
               'Demander le classement des joueurs pour les différents jeux',
               'Changer de mot de passe',
               'Se déconnecter']
    nb_options = len(options)

    def run(self):
        """
        Permet au joueur de choisir ses fonctionnalités.
        :return: renvoie au menu souhaité par l'utilisateur
        """
        print("Bienvenue " + str(Session.pseudo) + ", amusez-vous sur ---♥♦♣♠ Team22Games ♠♣♦♥--- !")
        print(MenuFonctionnalites.title2)
        for i, mes in enumerate(MenuFonctionnalites.options):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue
            if choice <= 0 or choice > MenuFonctionnalites.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                ControleurDemanderListeJeux.demander_liste_jeux()
                border()
                return MenuFonctionnalites()
                continue

            elif choice == 2:
                border()
                return MenuJeuxCreate()
                border()

            elif choice == 3:
                border()
                return MenuJeuxJoin()
                border()

            elif choice == 4:
                border()
                ControleurStat.demander_stat(Session.pseudo)
                border()
                return MenuFonctionnalites()
                continue

            elif choice == 5:
                border()
                return MenuJeuxClassement()
                border()

            elif choice == 6:
                border()
                return MenuModifierMdp.run(Session.pseudo)
                border()

            elif choice == 7:
                border()
                return MenuEtesVousSur()
                border()
