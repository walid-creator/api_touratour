from client.requetes.requete_grille import RequeteGrille

class MenuGrille:
    
    #Présente tous les menus utiles à la manipulation de la grille dans le jeu du morpion
        

    def recuperer(id_partie,nb_cases):
        #afficher la grille au joueur
        req = RequeteGrille.recuperer(id_partie,nb_cases)
        for i in range(len(req)):
            print(str(req[i])+"\n")

    def modifier(id_partie, numcase, valeur):
        # modification de la case
        return RequeteGrille.modifier(id_partie, numcase, valeur)

    def recupererPions(id_partie):
        # récupération des deux pions de la partie
        return RequeteGrille.recuperer(id_partie)

    def grillepleine(id_partie):
        #vérifie si la grille est pleine
        return RequeteGrille.pleine(id_partie)

    def alignergrille(id_partie,pion):
        #vérifie si un joueur a aligné ses pions 
        return RequeteGrille.alignergrille(id_partie,pion)

    def verif_case_pleine(id_partie, numcase):
        #vérifie si la case est pleine pour permettre à l'utilisateur de la joueur ou pas
        return RequeteGrille.verif_case_pleine(id_partie, numcase)
