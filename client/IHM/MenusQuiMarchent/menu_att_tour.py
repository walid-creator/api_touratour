from client.requetes.requete_get_parties import RequeteGetParties
from client.assets.assets import border, plier
from client.IHM.MenusQuiMarchent.Menu_Tour import MenuTour
from client.IHM.session import Session
import time


class MenuAttTour:


    def run(id_participant, id_partie):
        """
        Vérifier si c'est au tour du joueur de jouer.
        :param id_participant,id_partie : identifiants du participant et de la partie 
        :type id_participant,id_partie: integer
        """


        #get l'ordre(id_participant)

        x = 0
        a = 1

        while x == 0 :

            statutfin = int(RequeteGetParties.obtenir_statutfin(id_partie))

            if statutfin == 2:
                plier()
                # requete qui modifie les stats des joueurs qui ont perdu en fonction de leur id_participant
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()

            else:

                if a != int(RequeteGetParties.obtenir_numtour(id_partie)):
                    print("Format statut : \n"
                          "[Bornes, FEU, LIM, ESS, CRE, ACC, *PRI, *CIT, *INC, *VOL]")
                    for i in range(int(RequeteGetParties.get_param(id_partie)[0][1])):
                        id_particip = RequeteGetParties.obtenir_id_particip(id_partie, (i+1))
                        print('Le statut de ' + RequeteGetParties.obtenir_pseudo(id_particip) + ' : ')
                        print(RequeteGetParties.obtenir_statut(id_particip)[0])
                    carte = [RequeteGetParties.obtenir_derniere_carte_poubelle(id_partie)]
                    print('La dernière carte de la poubelle est : ', carte)
                    main = RequeteGetParties.obtenir_main(id_participant)
                    # MAIN = ["carte1","carte2","carte3","carte4","carte5","carte6", "carte7"]
                    MAIN = []
                    for i in range(int(len(main) / 4)):
                        MAIN += [main[4 * i: 4 * i + 4]]
                    print('Votre main : ', MAIN)
                    border()
                    x = RequeteGetParties.obtenir_sontour(id_participant)
                    time.sleep(5)
                    a = int(RequeteGetParties.obtenir_numtour(id_partie))
                else :
                    time.sleep(3)


        return(MenuTour.run(id_participant, id_partie))




    def runMorpion(id_participant, id_partie):
        if RequeteGetParties.obtenir_sontour(id_participant)==1:
            return True 
        else: 
            return False    
        
            





        #modulo !!
        #
        #en fonction de l'ordre --> update le sontour dans participant


        ## Boucle while + time.sleep : condition de sortie de boucle c'est à notre tour de jouer
                #tant qu'on est dans la boucle, on get et print les statuts de tout le monde (forme), même le sien
                #on renvoi la main du mec (id_participant)
                #on renvoi la dernière carte de la poubelle(id_partie)

        #on est sorti de la boucle
        #return Menu_Tour
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#             a = ControleurPartie.get_Participants(id_partie)
#             b = int(ControleurPartie.get_Param(id_partie))
#
#             while len(a) != b:
#                 border()
#                 print("Voici la liste des joueurs ayant déjà rejoint la partie")
#                 for i in range(len(a)):
#                     print(a[i][0])
#                 print("Nous attendons encore la venue de " + str(b - len(a)) + " joueur(s)")
#                 a = ControleurPartie.get_Participants(id_partie)
#                 time.sleep(3)
#
#             if Session.pseudo == a[0][0]:
#                 return MenuAttDepart.ordonner(id_partie, b, a)
#
#             else:
#                 print('La partie va commencer, veuillez patienter ...')
#                 id_participant = RequeteGetParties.get_id_participant(id_partie, Session.pseudo)[0][0]
#                 time.sleep(20)
#                 border()
#                 reglesMilleB()
#                 border()
#                 return MenuAttTour(id_participant, id_partie)
#
#         def ordonner(id_partie, b, a):
#
#             L = []
#             for i in range(b):
#                 L += [i]
#             r.shuffle(L)
#
#             for i in range(b):
#                 # poster le numero partie, nvordre = L[i], ordre = i
#                 # update sur le participant ayant l'ordre i sur la partie on lui met L[i]
#                 pseudo = a[i][0]
#                 RequeteGetParties.donner_ordre(id_partie, L[i], pseudo)
#
#             RequeteGetParties.create_pioche(id_partie)
#             RequeteGetParties.create_poubelle(
#                 id_partie)  # create pioche et poubelle (utiliser le métier) avec l'id_partie
#
#             liste_part = RequeteGetParties.get_all_id_participant(id_partie)
#             for i in range(len(liste_part)):
#                 id_participant = liste_part[i][0]
#                 RequeteGetParties.creer_main(id_participant)
#                 RequeteGetParties.creer_statut(id_participant)
#                 # initialise les mains, les statuts de tous les joueurs avec l'id_participant
#
#             print("La partie va commencer ...")
#             border()
#             reglesMilleB()
#             border()
#             return MenuAttTour(a[0][0], id_partie)


    def runMorpion(id_partie):
         """
        Vérifier si c'est au tour du joueur de jouer.
        :param id_participant,id_partie : identifiants du participant et de la partie 
        :type id_participant,id_partie: integer
        :return: si c'est son tour de jouer
        :rtype: booléen 
        """
        id_participant=int(RequeteGetParties.get_id_participant(id_partie,Session.pseudo)[0][0])
        if RequeteGetParties.obtenir_sontour(id_participant)==1:
            return True
        else:
            return False
