from serveur.dao.classe_participant_dao import ParticipantDao

class ServiceModifTour:
    def modif_tour(id_participant,tour):
        return ParticipantDao.modif_tour(id_participant,tour)
