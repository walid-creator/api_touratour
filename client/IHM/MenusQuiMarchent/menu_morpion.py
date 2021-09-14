import random
from client.IHM.MenusQuiMarchent.menu_tour_a_tour import TourATourMorp
from client.IHM.MenusQuiMarchent.menu_grille import MenuRecupererGrille
from client.IHM.MenusQuiMarchent.menugrille import MenuModifierGrille

class MenuMorpion:
    def run():
        print("Bonjour! En route pour le jeu de morpion!")
        if  #acréé une partie:
            nbrcases = int(input("Avec quel nombre de cases voulez-vous jouer ? "))
            nbjoueurs = 2
            # type de pion affectÈ ‡ chaque joueur.
            pions = input("Veuillez saisir le pion que vous voulez : ")  #
            # choix de la langue
            #print("Quelle langue voulez-vous choisir?")
            #print(u"[1] Français")
            #print(u"[2] Espagnol")
            #print(u"[3] Italien")
            #Langue = input("")

            # dÈfinir celui qui commence, ou dÈfinir au hasard #pour le créateur de la partie
            print(u"Définir qui va commencer")
            print(u"[1] le joueur 1 commence")
            print(u"[2] le joueur 2 commence")
            print(u"[3] le joueur qui commence est défini au hasard")
            x = int(input(u"Quel choix voulez-vous? [3 par defaut]: "))
            if x==1:
                premier = 0
            elif x==2:
                premier = 1
            else:
                premier = random.randint(0, nbjoueurs - 1)
            # if rejoindre une partie

            print("=====> c'est joueur" + str(premier + 1) + " qui commence")

            print("la partie commence ! ")


            #créer un menu grille pleine qui vérifie si la grille est pleine ou pas
            MenuGrille.creer(nbrcases)#

            while MenuGrillepleine.run() == False :
                MenuFinPartieMorpion.run(pions)
                break
            else:
                print("Pas de gagnant")


        else:
            #a rejoint une partie
            print("Bonjour! En route pour le jeu de morpion!")
            pions = input("Veuillez saisir le pion que vous voulez : ")
            print("la partie commence ! ")
            MenuGrille().creer(nbrcases)
            while MenuGrillepleine.run() == False:
                MenuFinPartieMorpion.run(pions)
                break
            else:
                print("Pas de gagnant")


           