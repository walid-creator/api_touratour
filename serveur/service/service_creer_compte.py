from serveur.dao.classe_joueur_dao import JoueurDao
from serveur.dao.classe_statistiques_dao import StatistiquesDao
from serveur.dao.classe_jeu_dao import JeuDao


########## Classe session ###########

class ServiceCreerCompte:

    def verifSiDejaPseudo(nvPseudo):
        """
        Vérifie si déjà pseudo dans la base
        :param nvPseudo: nouveau pseudo à ajouter
        :type nvPseudo: chaine de caractères
        :return: 0,1 ou 2
        :rtype: int
        """
        taille_base = len(JoueurDao.read_all())
        res = 0
        liste = JoueurDao.read_all()
        if len(nvPseudo) >= 25:
            return 0
        else:
            for i in range(taille_base):
                if str(nvPseudo) == liste[i][1]:
                    res = res + 1
                else:
                    res = res + 0
            if res > 0:
                return 1
            else:                
                return 2
    
    def verifMdp(nvPseudo, nvMdp):
        """
        Vérifie si mdp vérifie les contraintes et ajoute le joueur
        param nvMdp: nouveau pseudo à ajouter au nouveau joueur
        :type nvMdp: chaine de caractères
        :return: 0, 1 ou 2
        :rtype: int
        """
        m = 0
        for i in range(len(JoueurDao.read_all())):
            if int(JoueurDao.read_all()[i][0]) > m:
                m = int(JoueurDao.read_all()[i][0])
        nv_taille = m+1
        if len(nvMdp) < 10:
            return 0
        else:
            JoueurDao.create(nv_taille, nvPseudo, nvMdp) ### création du joueur dans la base
            return ServiceCreerCompte.init_stat(nvPseudo)

    def init_stat(pseudo):
        taille_base_stat = len(StatistiquesDao.read_all())
        taille_base_jeu = len(JeuDao.read_all())
        for i in range(taille_base_jeu):    ### initialisation des statistiques des joueurs en fonction des jeux
            nv_taille_stat = taille_base_stat+i+1
            id_jeu = i+1
            StatistiquesDao.create(nv_taille_stat, pseudo, id_jeu,  0, None, 0, 0)
        return 1