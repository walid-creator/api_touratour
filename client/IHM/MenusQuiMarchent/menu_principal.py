from client.IHM.MenusQuiMarchent.menu_connexion import MenuConnexion
from client.IHM.MenusQuiMarchent.menu_creer_compte import MenuCreerCompte
from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
from client.controleur.controleur_demander_liste_jeux import ControleurDemanderListeJeux
from client.assets.assets import border,vache, plier

# Menu principal

class MenuPrincipal():
    

    title = 'Bienvenue sur ---♥♦♣♠ Team22Games ♠♣♦♥---\n Que voulez-vous faire ?'
    options = ['Créer un compte','Se connecter','Demander la liste des jeux', "Quitter l'application"]
    nb_options = len(options)

    def run(self):
        """
        Les différentes actions que l'utilisateur de application peut faire.
        :return: le menu choisi par l'utilisateur
        """

        # lancement du menu et affiche la question principale du menu
        print(MenuPrincipal.title)

        # format de l'affichage du menu
        for i, mes in enumerate(MenuPrincipal.options):
            print("[{}] {}".format(i + 1, mes))

        # l'utilisateur choisit une option
        while True :
            choice = input('\n saisissez votre réponse : ')

            try :
                choice = int(choice)

            except ValueError :
                print("La valeur attendue doit être un entier")
                continue

            if choice <=0 or choice > MenuPrincipal.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                return MenuCreerCompte.run()
                border()

            elif choice == 2:
                border()
                return MenuConnexion.run()
                border()

            elif choice == 3:
                border()
                ControleurDemanderListeJeux.demander_liste_jeux()
                border()
                return MenuPrincipal()
                continue
                
            elif choice == 4:
                vache()
                break
