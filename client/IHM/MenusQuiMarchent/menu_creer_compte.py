from client.requetes.requete_creer_compte import RequeteCreerCompte

class MenuCreerCompte():
    title = 'Portail de création de compte'

    def run():
        """
        vérifie si le pseudo est déjà existant et qui vérifie certaines conditions
        :return: renvoie au menu qui permet d'ajouter le compte à la base de données
        (la fonction au dessous)
        """

        print(MenuCreerCompte.title)
        print("[{}] {}".format(1, "Choisissez votre pseudo"))
        print("[{}] {}".format(2, "Revenir au menu précédent"))
        choice= input("")
        if choice == "1":
            pseudo = input('Veuillez entrer votre pseudo : ')
            if RequeteCreerCompte.TesterPseudo(pseudo) == 0:
                print("Votre pseudo doit être inférieur à 25 caractères")
                return MenuCreerCompte.run()
            elif RequeteCreerCompte.TesterPseudo(pseudo) == 1:
                print("Pseudo déjà existant, veuillez entrer un pseudo valide")
                return MenuCreerCompte.run()
            elif RequeteCreerCompte.TesterPseudo(pseudo) == 2:
                print("Pseudo valide")
                return MenuCreerCompte.run2(pseudo)
            else:
                print("Erreur, retour au menu principal")
                from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
                return MenuPrincipal()
        else:
            from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
            return MenuPrincipal()        

    def run2(pseudo):
        """
        Vérifie si le mot de passe vérifie des conditions pour une question de sécurité
        et ajoute le compte à la base de données.
        :param pseudo: le pseudo du compte
        :type pseudo: string
        :return: renvoie au menu principal
        """

        mdp = input("Veuillez enter un mot de passe : ")
        mdp = str(mdp)
        requete = RequeteCreerCompte.CreerCompte(pseudo, mdp)
        if requete == 0:
            print("Votre mot de passe doit être supérieur à 10 caractères, que voulez-vous faire ?")
            print("[{}] {}".format(1, "Réessayer"))
            print("[{}] {}".format(2, "Revenir au menu précédent"))
            choice= input("")
            if choice=="1":
                return MenuCreerCompte.run2(pseudo) 
            else:
                from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
                return MenuPrincipal()     
            
        elif requete == 1:
            print("Votre compte a bien été créé, vous allez être redirigé sur le menu principal")
            from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
            return MenuPrincipal()
        else:
            print("Erreur, retour au menu principal")
            from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
            return MenuPrincipal()
