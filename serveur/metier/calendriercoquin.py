
class calendriercoquin:
    """
    deux méthodes : une qui vérifie si on peut jouer la carte et une autre qui modifie le statut en cas ou c'est oui
    """


    def peut_on_jouer_calendriercoquin(statut, participant):
        L = statut
        if participant == L[0]:
            return 1
        else:
            return 0


    def jouer_calendriercoquin(statut):
        L = statut
        res = [L[0],L[1],1,1,L[4],L[5],L[6],1,L[8],L[9],L[10]]
        return res
