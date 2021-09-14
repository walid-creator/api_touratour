from client.IHM.MenusQuiMarchent.start import Start

# Point d'entrée de notre application.

if __name__ == '__main__':
    # on démarre sur l'écran accueil
    current_vue = Start()

    # tant qu'on a un écran à afficher, on continue
    while current_vue:
        current_vue = current_vue.run()
