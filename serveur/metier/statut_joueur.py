class Statut:
    """
    attribus :
    id participant : int

    list :
    participant
    nombre de bornes : int ( de 0 a 1000)
    feu rouge : int (0 ou 1)
    limite vitesse : int (0 ou 1)
    panne essence : int (0 ou 1)
    crevaison : int (0 ou 1)
    accident : int (0 ou 1)
    botte_pompier : int (0 ou 1)
    botte_citerne : int (0 ou 1)
    botte_roue : int (0 ou 1)
    botte_volant: int (0 ou 1)

    Dans tous les cas 0 = rouge et 1 = vert
    methode :
    -modifier_statut()
    -donner_statut(participant)
    """

    def __init__(self, statut):
        self.statut = statut

    def donner_statut(participant):
        pass
        #la une methode get qui va rendre la liste des attributs qu'on a stocke dans la table StatutJoueur

    def modifier_statut(carte, participant, joueurVise):
        pass


        #la une methode qui verifie si l'on peut jouer cette carte sur ce participant
        #Elle return "vous ne pouvez pas jouer cette carte sur ce joueur" si c'est non
        #Elle return le nouveau statut si c'est oui