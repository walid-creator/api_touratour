
class Borne25:
    """
    deux méthodes : une qui vérifie si on peut jouer la carte 25B et une autre qui modifie le statut en cas ou c'est oui
    """


    def peut_on_jouer_25B(statut, participant):
        # fonction qui renvoie 0 si on ne peut pas jouer la carte sur le joueur, qui renvoie 1 si oui
        # on peut jouer cette carte seulement si on la joue sur nous meme.
        # on peut jouer cette carte seulement si le produit des cellules 2 par 4 par 5 par 6 vaut 1

        L = statut

        if L[2]*L[4]*L[5]*L[6] == 1:
            if participant == L[0]:
                return 1
        else:
            return 0


    def jouer_25B(statut):
        L = statut
        res = [L[0],L[1] + 25,L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10]]
        return res



