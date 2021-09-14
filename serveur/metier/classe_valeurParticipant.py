class ValeurParticipant:
    def __init__(self, id_valeurParticipation, id_paramParticip, id_participant, ordreParticipant, valeurParticipant):
        self.id_valeurParticipation = id_valeurParticipation
        self.id_paramParticip =  id_paramParticip
        self.id_participant = id_participant
        self.ordreParticipant = ordreParticipant
        self.ordreParticipant = ordreParticipant
        self.valeurParticipant = valeurParticipant
        
    def __str__(self):
        return(" id_paramParticip : {}// id_participant : {} // valPriseAssoParam: {}".format(self.id_paramParticip, self.id_participant,  self.valeurParticipant))    
 

class ValeursParticipant: #juste pour récupérer les paramètres et les afficher pour une partie
    def __init__(self, id_participant,id_joueur, id_partie):
        self.id_participant = id_participant
        self.id_partie = id_partie
        self.liste = []
    
    def choixvalsparam(self, ValeurParticipant):
        if self.id_participant==ValeurParticipant.id_participant:
            self.liste.append(ValeurParticipant) 
            return ValeursParticipantDao.create(ValeurParticipant)
