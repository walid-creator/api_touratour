
class pneuMichelin:
    """
    deux méthodes : une qui vérifie si on peut jouer la carte panne et une autre qui modifie le statut en cas ou c'est oui
    """


    def peut_on_jouer_pneuMichelin(statut, participant):
        L = statut
        if participant == L[0]:
            return 1
        else:
            return 0


    def jouer_pneuMichelin(statut):
        L = statut
        res = [L[0],L[1],L[2],L[3],L[4],1,L[6],L[7],L[8],1,L[10]]
        return res