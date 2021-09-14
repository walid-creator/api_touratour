from client.IHM.MenusQuiMarchent.menu_grille import MenuGrille
from client.IHM.MenusQuiMarchent.menu_tour_a_tour import TourATourMorp
from client.controleur.controleur_case import ControleurCase
from client.IHM.MenusQuiMarchent import trad
from client.controleur.controleur_pion import ControleurPion
from client.assets.assets import border

class MenuPartieMorpion:
    def run(pion, Langue,id_partie):
        """
        Le déroulement de la partie du morpion.
        :param pion, Langue, id_partie 
        :type param: string, integer et integer respectivement
        """

        t = (1, 2, 3, 4, 5, 6)
        for j in t:
            if Langue == j:
                pion2 = ControleurPion.recup_pion(id_partie)
                pion1= ControleurPion.recup_pion1(id_partie)
                if pion==pion1:
                    pionautre=pion2
                else:
                    pionautre=pion1
                #vérifie si la grille est pleine, ou l'un des joueurs a gagné (codition d'arrêt de la partie)   
                while MenuGrille.grillepleine(id_partie) == False and MenuGrille.alignergrille(id_partie,pion1) == False and MenuGrille.alignergrille(id_partie,pion2) == False:
                    #récupérer le nombre de case de la grille
                    nbcases=int(ControleurCase.recup_nbcases(id_partie))
                    # afficher la grille à l'utilisateur
                    MenuGrille.recuperer(id_partie,nbcases)
                    # jouer ou quitter la partie
                    return TourATourMorp(id_partie,Langue,pion).run()

                else:
                    if MenuGrille.alignergrille(id_partie,pion) == True:
                        # si le pion du joueur connecté a gangné 
                        print(trad.gagne[j-1])
                    elif MenuGrille.grillepleine(id_partie) == True:
                        #si la grille est pleine sans gagant
                        print(trad.aucun[j-1])
                    else:
                         # si le pion de l'autre joueur a gagneé ie notre joueur a perdu
                        print(trad.perdu[j-1])
                    border()
                    from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                    return MenuFonctionnalites()


            else:
                j=1
