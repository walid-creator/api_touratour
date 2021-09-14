from client.assets.assets import border
from client.IHM.session import Session


class MenuEtesVousSur():
    title = 'En êtes-vous sûr ?'
    options = ["Oui",
               "Non"]
    nb_options = len(options)

    def run(self):

        print(MenuEtesVousSur.title)

        for i, mes in enumerate(MenuEtesVousSur.options):
            print("[{}] {}".format(i + 1, mes))

        while True:
            choice = input('\n saisissez votre réponse : ')

            try:
                choice = int(choice)

            except ValueError:
                print("La valeur attendue doit être un entier")
                continue
            if choice <= 0 or choice > MenuEtesVousSur.nb_options:
                print("Petit blagueur")
                continue

            elif choice == 1:
                border()
                Session.pseudo = "zefq"
                from client.IHM.MenusQuiMarchent.menu_principal import  MenuPrincipal
                return MenuPrincipal()
                border()

            elif choice == 2:
                border()
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
                border()




