from client.requetes.requete_modifier_mdp import RequeteModifierMdp
from client.IHM.MenusQuiMarchent.abstract_menu import AbstractMenu
from client.assets.assets import border


class MenuModifierMdp:
    title = 'Portail de modification de compte'

    def run(pseudo):
        """
        Modifier le mot de passe d'un joueur.
        :param pseudo: pseudo du joueur 
        :type pseudo: string
        :return: renvoie au menu des fonctionnalités
        """
        print(MenuModifierMdp.title)
        nvMdp = input("Veuillez entrer votre nouveau mot de passe : ")
        if len(nvMdp)<10:
            print("Votre mot de passe doit avoir plus que 10 caractères")
            return MenuModifierMdp.run(pseudo)
        else:
            if RequeteModifierMdp.modifier_mdp(pseudo, nvMdp) == True:
                print("Votre mot de passe a bien été modifié")
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
            else:
                print("La modification a échoué ")
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()

