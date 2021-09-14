from client.IHM.MenusQuiMarchent.menu_principal import MenuPrincipal
from client.assets.assets import banner


class Start():
# menu de demarrage et lance le menu principal
    def __init__(self, hello = True):
        # construction du menu 
        #hello : indique s'il faut afficher ou non le message de bienvenue
        self.hello = hello

    def run(self):
        # lancement du menu et affiche le message de bienvenue
        if self.hello:
            banner()

        return MenuPrincipal()


