
class joquatari:
    """
    deux méthodes : une qui vérifie si on peut jouer la carte et une autre qui modifie le statut en cas ou c'est oui
    """


    def peut_on_jouer_joquatari(statut, participant):
        L = statut
        if participant == L[0]:
            return 1
        else:
            return 0


    def jouer_joquatari(statut):
        L = statut
        res = [L[0],L[1],L[2],L[3],1,L[5],L[6],L[7],1,L[9],L[10]]
        return res