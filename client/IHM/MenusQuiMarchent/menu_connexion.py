from client.requetes.requete_connexion import RequeteConnexion
from client.IHM.session import Session
from client.assets.assets import border



class MenuConnexion():
    title = 'Portail de connexion'

    def run():
        """
        Permettre au joueur de se connecter. 
        :return: renvoie au menu attendre tour
        :rtype: bool pour le morpion
        renvoie au menu aux fonctionnalités
        """
        print(MenuConnexion.title)
        border()
        pseudo = input('Entrer votre pseudo : \n')
        mdp = input('Entrer votre mot de passe : \n')
        border()
        if RequeteConnexion.connexion(pseudo,mdp) == False:
            print("Pseudo ou mot de passe incorrect, que voulez-vous faire ?\n")
            print("[{}] {}".format(1, "Se reconnecter\n"))
            print("[{}] {}".format(2, "Revenir au menu précédent\n"))
            choice= input("")
            if choice=="1":
                
                return MenuConnexion.run()
            else:
                from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
                return MenuPrincipal()
        else:
            print("Connexion réussie")
            border()
            Session.pseudo = pseudo
            # retourne le menu des fonctionnalités
            from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
            return MenuFonctionnalites()
