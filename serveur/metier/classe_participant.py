########## Classe Participant ###########

class Participant:
    def __init__(self,id_participant, id_partie, pseudo, ordre, enjeu, score, classement, sontour):
        self.id_participant = id_participant
        self.id_partie = id_partie
        self.pseudo = pseudo
        self.ordre = ordre
        self.enjeu = enjeu
        self.score = score
        self.classement = classement
        self.sontour = sontour
