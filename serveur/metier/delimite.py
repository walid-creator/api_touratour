
class delimite:
    """
    deux méthodes : une qui vérifie si on peut jouer la carte delimite et une autre qui modifie le statut en cas ou c'est oui
    """


    def peut_on_jouer_delimite(statut, participant):
        # fonction qui renvoie 0 si on ne peut pas jouer la carte sur le joueur, qui renvoie 1 si oui
        # on peut jouer cette carte seulement si on la joue pas sur nous meme.
        # on peut jouer cette carte seulement si la cellule 3 est a 1
        # on peut jouer cette carte seulemet si la cellule 10 est a 0

        L = statut

        if L[3] == 0 and L[10] == 0:
            if participant == L[0]:
                return 1
        else:
            return 0


    def jouer_delimite(statut):
        L = statut
        res = [L[0],L[1],L[2],1,L[4],L[5],L[6],L[7],L[8],L[9],L[10]]
        return res
