from client.assets.assets import border
from client.controleur.controleur_partie import ControleurPartie
from client.IHM.session import Session
from client.requetes.requete_get_parties import RequeteGetParties
from client.IHM.MenusQuiMarchent.menu_attente import MenuAttDepart
from client.controleur.controleur_langue import ControleurLangue
from client.controleur.controleur_pion import ControleurPion
from client.controleur.controleur_premier import ControleurPremier


class MenuRejoindrePartie:

    def run(jeu):

        ControleurPartie.demander_parties(jeu)
        border()
        choix = input("Quelle partie souhaitez-vous rejoindre ? (entrez l'id de la partie) \n ")
        l = []
        h = RequeteGetParties.demander_parties(jeu)
        for i in range(len(h)):
            l += [h[i][0]]
        if (int(choix) not in l) != True:
            req = ControleurPartie.choisir_partie(choix, jeu, Session.pseudo)
            if req == True:
                print('Vous entrez dans la partie \n')
                return MenuAttDepart.run(choix)
            else :
                print('Erreur, retour au menu des fonctionnalités \n')
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
        else:
            print('Vous devez choisir un identifiant valide \n')
            from client.IHM.MenusQuiMarchent.menu_jeux import MenuJeuxJoin
            return MenuJeuxJoin()
        border()

    def runM(jeu):

        ControleurPartie.demander_partiesM(jeu)
        border()
        choix = input("Quelle partie souhaitez-vous rejoindre ? (entrez l'id de la partie) \n ")
        l = []
        h = RequeteGetParties.demander_partiesM(jeu)
        for i in range(len(h)):
            l += [h[i][0]]
        if (int(choix) not in l) != True:
            req = ControleurPartie.choisir_partie(choix, jeu, Session.pseudo)
            if req == True:
                print('Vous entrez dans la partie \n')
                Langue=int(ControleurLangue.recup_langue(choix))
                pion=ControleurPion.recup_pion(choix)
                premier=int(ControleurPremier.recup_premier(choix))
                return MenuAttDepart.runMorpion(choix,Langue,pion,premier)
            else :
                print('Erreur, retour au menu des fonctionnalités \n')
                from client.IHM.MenusQuiMarchent.menu_fonctionnalites import MenuFonctionnalites
                return MenuFonctionnalites()
        else:
            print('Vous devez choisir un identifiant valide \n')
            from client.IHM.MenusQuiMarchent.menu_jeux import MenuJeuxJoin
            return MenuJeuxJoin()
        border()


