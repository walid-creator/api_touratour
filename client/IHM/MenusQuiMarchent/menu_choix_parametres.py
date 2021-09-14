from client.controleur.controleur_partie import ControleurPartie
from client.IHM.session import Session
from client.assets.assets import border
from client.IHM.MenusQuiMarchent.menu_attente import MenuAttDepart
from client.controleur.controleur_param import ControleurParam
from client.IHM.MenusQuiMarchent import trad

import random


class MenuChoixParametres():
    title = 'Vous avez choisi de créer une partie, maintenant, il faut les paramètres !'

    def run(choice):

        print(MenuChoixParametres.title)

        if choice == 1:
            #Choix de la langue
            border()
            print("Quelle langue voulez-vous choisir?")
            print("[1] Français")
            print("[2] Espagnol")
            print("[3] Italien")
            print("[4] Anglais")
            print("[5] Lituanien")
            print("[6] Néerlandais")
            Langue = int(input("Quelle langue voulez-vous? [1 par defaut]: "))

            t = (1, 2, 3, 4,5,6)
            for i in t:
                if Langue == i:
                    border()
                    nbrcases = int(input(trad.cases[i-1]))
                    if nbrcases != 9 and nbrcases != 16 and nbrcases != 25:
                        nbrcases = int(input(trad.rpcases[i-1]))
                    border()
                    pions1 = input(trad.p1[i-1])
                    border()
                    pions2 = input(trad.p2[i-1])
                    if pions1 == pions2:
                        pions2 = input(trad.ep2[i-1])
                    border()
                    print(trad.begin[i-1] + "\n" + trad.beginj1[i-1]+ "\n" + trad.beginj2[i-1]+ "\n"+ trad.beginrandom[i-1])
                    x = int(input(trad.choicex[i-1]))

                else:
                    i=1


            nbjoueurs = 2

            # dÈfinir celui qui commence, ou dÈfinir au hasard #pour le créateur de la partie
            if x == 1:
                premier = 0
            elif x == 2:
                premier = 1
            else:
                premier = random.randint(0, nbjoueurs - 1)

            val=[Langue,nbrcases,pions1,pions2,premier]
            req = ControleurPartie.creer_partie(choice, Session.pseudo, nbjoueurs)
            ControleurParam.creer_paramM(req,val)
            return MenuAttDepart.runMorpion(req,Langue,pions1,premier)



        elif choice == 2:
            while True:
                C = input('\n Combien de joueurs dans la partie? ')
                try:
                    C = int(C)
                except ValueError:
                    print("La valeur attendue doit être un entier")
                    continue
                if C <= 1:
                    print("Petit blagueur")
                    continue
                elif C > 4:
                    print(" le 1000Bornes se joue au maximum à quatres joueurs")
                    continue
                else:
                    req = ControleurPartie.creer_partie(choice, Session.pseudo, C)
                    print('Votre partie est bien créée, veuillez attendre les autres joueurs')
                    border()
                    return MenuAttDepart.run(req)

        else:
            print('erreur')
