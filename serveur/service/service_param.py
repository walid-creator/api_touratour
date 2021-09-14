from serveur.dao.classe_valeurPartie_dao import ValeurPartieDao
from serveur.dao.classe_paramPartie_dao import ParamPartieDao

class ServiceParam:
    def creer_param(id_partie, valeur):
        taille_param = len(ValeurPartieDao.read_all())
        taille_base_param = len(ParamPartieDao.read_all())
        # créer parametre
        for i in range(taille_base_param):
            nv_taille_param=taille_param+i+1
            id_para=i+1
            ValeurPartieDao.create(nv_taille_param, id_para, id_partie,0, valeur[i])
        return True
