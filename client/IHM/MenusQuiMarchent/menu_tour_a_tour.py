from client.IHM.MenusQuiMarchent.menu_att_tour import MenuAttTour
from client.controleur.controleur_pion import ControleurPion
from client.controleur.controleur_case import ControleurCase
from client.IHM.MenusQuiMarchent import trad
from client.IHM.MenusQuiMarchent.menu_grille import MenuGrille
from client.requetes.requete_montour import ModifTour
from client.IHM.session import Session
from client.requetes.requete_get_parties import RequeteGetParties
import time
from client.assets.assets import border

#
#
class TourATourMorp():
    def __init__(self,id_partie,Langue, pion):
         self.id_partie = id_partie
         self.Langue = Langue #langue choisie
         self.pion=pion #le symbole du pion

    def run(self):
        
        #Le déroulement d'un tour du joueur du morpion
        


        t = (1, 2, 3, 4, 5, 6)
        for j in t:
            if self.Langue == j:#choix de la langue

                options = [trad.o1[j-1],
                           trad.o2[j-1]]
                nb_options = len(options)
                print(trad.tour[j-1])
                for i, mes in enumerate(options):
                    print("[{}] {}".format(i + 1, mes))
                while True:
                    choice = input(trad.rep[j-1])
                    try:
                        choice = int(choice)

                    except ValueError:
                        print((trad.err[j-1]))
                        continue
                    if choice <= 0 or choice > nb_options:
                        print(trad.joke[j-1])
                        continue
                    elif choice == 1: #choix du francais
                        nb_cases = int(ControleurCase.recup_nbcases(self.id_partie))
                        while MenuAttTour.runMorpion(self.id_partie) == False:
                            print(trad.att2[j - 1])
                            time.sleep(5)
                        MenuGrille.recuperer(self.id_partie, nb_cases)#récupéper la grille
                        print(trad.num[j - 1].format(nb_cases - 1))
                        numcase = int(input())
                        while MenuGrille.verif_case_pleine(self.id_partie,numcase)==True:
                            # vérifie si la case demandée par le joueur est pleine
                             numcase = int(input(trad.verif[j-1]))
                        while numcase > nb_cases - 1:# nb_cases=9,16 ou 25 
                             numcase = int(input(trad.err2[j - 1]))
                        MenuGrille.modifier(self.id_partie, numcase, self.pion) # on ajoute le pion à la grille
                        id_participant = int(RequeteGetParties.get_id_participant(self.id_partie, Session.pseudo)[0][0])
                        ModifTour.modif_tour(id_participant, 0)# on modifie le tour du partcicipant à 0 après avoir joué
                        #récupère les id des particpants
                        id_participants2 = RequeteGetParties.get_all_id_participant(self.id_partie)
                        if id_participant == id_participants2[0][0]: 
                             id_participant2 = id_participants2[1][0] 
                        else:
                             id_participant2 = id_participants2[0][0]
                        # on récupère l'identifiant de l'autre participant et on modifie son tour pour qu'il puisse 
                        #jouer     
                        ModifTour.modif_tour(id_participant2, 1)

                        from client.IHM.MenusQuiMarchent.menu_partie_morpion import MenuPartieMorpion
                        #on renvoie au menu  du morpion
                        return MenuPartieMorpion.run(self.pion, self.Langue, self.id_partie)

                    elif choice == 2:
                        # à chaque tour on propose au joueur s'il veut jouer ou abondonner la partie
                        #dans le dernier cas on le renvoie  au menu principal
                        border()
                        from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                        return MenuFonctionnalites()

            else:
                j=1

