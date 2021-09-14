from client.controleur.controleur_partie import ControleurPartie
import time
from client.assets.assets import border, reglesMilleB, plier
from client.IHM.session import Session
import random as r
from client.requetes.requete_get_parties import RequeteGetParties
from client.IHM.MenusQuiMarchent.menu_att_tour import MenuAttTour
from client.IHM.MenusQuiMarchent import trad
from client.IHM.MenusQuiMarchent.menu_partie_morpion import MenuPartieMorpion
from client.requetes.requete_montour import ModifTour

class MenuAttDepart:
    

    def run(id_partie):
         """
        Attendre la venue des autres joueurs et commence la partie.
        :param id_partie,: identifiants de la partie 
        :type id_partie: integer
        :return: renvoie au menu attendre tour
        :rtype: bool pour le morpion
        """

        a = ControleurPartie.get_Participants(id_partie)
        b = int(ControleurPartie.get_Param(id_partie))

        while len(a) != b:
            border()
            print( "Voici la liste des joueurs ayant déjà rejoint la partie")
            for i in range(len(a)):
                print(a[i][0])
            print("Nous attendons encore la venue de " + str(b-len(a)) + " joueur(s)")
            a = ControleurPartie.get_Participants(id_partie)
            time.sleep(3)

        if Session.pseudo == a[0][0]:
            return MenuAttDepart.ordonner(id_partie, b, a)

        else:
            print('La partie va commencer, veuillez patienter ...')
            id_participant = RequeteGetParties.get_id_participant(id_partie, Session.pseudo)[0][0]
            time.sleep(10)
            border()
            reglesMilleB()
            border()
            return MenuAttTour.run(id_participant, id_partie)

    def runMorpion(id_partie,Langue,pion,premier):
        """
        Attendre la venue des autres joueurs et commence la partie.
        :param id_partie,: identifiants de la partie 
        :type id_partie: integer
        """

        a = ControleurPartie.get_Participants(id_partie)
        b = int(ControleurPartie.get_Param(id_partie))

        t = (1, 2, 3, 4, 5, 6)
        for j in t:
            if Langue == j:#choix de la langue
                while len(a) != b:
                    border()
                    print(trad.ljoueur[j-1])
                    for i in range(len(a)):
                        print(a[i][0])
                    print(trad.att[j-1] + str(b-len(a)) + trad.joueur[j-1])
                    a = ControleurPartie.get_Participants(id_partie)
                    time.sleep(3)
                border()
                print(trad.pat[j-1])
                time.sleep(5)
                border()
                id_participants2 = RequeteGetParties.get_all_id_participant(id_partie)
                id_participant=min(int(id_participants2[0][0]),int(id_participants2[1][0]))
                id_participant2=max(int(id_participants2[0][0]),int(id_participants2[1][0]))
                if premier==0:
                    #mettre le sontour à 1 pour celui qui va jouer en premier et l'autre à 0
                    ModifTour.modif_tour(id_participant,1)
                else:
                    ModifTour.modif_tour(id_participant2, 1)

                return MenuPartieMorpion.run(pion,Langue,id_partie)
            else:
                j=1




    def ordonner(id_partie, b, a):

        L = []
        for i in range(b):
            L += [i]
        r.shuffle(L)

        for i in range(b):
            # poster le numero partie, nvordre = L[i], ordre = i
            # update sur le participant ayant l'ordre i sur la partie on lui met L[i]
            pseudo = a[i][0]
            RequeteGetParties.donner_ordre(id_partie, int((L[i]+1)), pseudo)

        RequeteGetParties.create_pioche(id_partie)
        RequeteGetParties.create_poubelle(id_partie) # create pioche et poubelle (utiliser le métier) avec l'id_partie


        liste_part = RequeteGetParties.get_all_id_participant(id_partie)
        for i in range(len(liste_part)):
            id_participant = liste_part[i][0]
            RequeteGetParties.creer_main(id_participant)
            RequeteGetParties.creer_statut(id_participant)
            # initialise les mains, les statuts de tous les joueurs avec l'id_participant

        id_participant = liste_part[0][0]

        print("La partie va commencer ...")
        border()
        reglesMilleB()
        border()
        return MenuAttTour.run(id_participant, id_partie)
