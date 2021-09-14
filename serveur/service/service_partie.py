from serveur.dao.classe_partie_dao import PartieDao
from serveur.dao.classe_participant_dao import ParticipantDao
from serveur.metier.classe_partie import Partie
from serveur.metier.classe_participant import Participant
from serveur.metier.pioche import Pioche
from serveur.metier.poubelle import Poubelle
from serveur.dao.classe_pioche_dao import PiocheDao
from serveur.dao.classe_poubelle_dao import PoubelleDao
from serveur.dao.classe_main_dao import MainDao
from serveur.metier.main_joueur import Main
from serveur.metier.statut_joueur import Statut
from serveur.dao.classe_statut_dao import StatutDao
from serveur.metier.borne_25 import Borne25
from serveur.metier.borne_50 import Borne50
from serveur.metier.borne_75 import Borne75
from serveur.metier.borne_100 import Borne100
from serveur.metier.borne_200 import Borne200
from serveur.metier.accident import accident
from serveur.metier.calendriercoquin import calendriercoquin
from serveur.metier.delimite import delimite
from serveur.metier.essence import essence
from serveur.metier.feuRouge import feuRouge
from serveur.metier.feuVert import feuVert
from serveur.metier.joquatari import joquatari
from serveur.metier.limite import limite
from serveur.metier.panne import panne
from serveur.metier.pneucreve import pneucreve
from serveur.metier.pneuneuf import pneuneuf
from serveur.metier.pneuMichelin import pneuMichelin
from serveur.metier.reparation import reparation
from serveur.metier.sebLoeb import sebLoeb
import random
from serveur.dao.classe_statistiques_dao import StatistiquesDao




class ServicePartie:
    
    def obtenir_parties(jeu):

        return PartieDao.read_all_att(jeu)

    def obtenir_partiesM(jeu):
        return PartieDao.read_all_attM(jeu)


    def choisir_partie(id_partie, jeu, pseudo):

        #update partie dans base
        totaljoueur = int(PartieDao.read(id_partie)[0][1])
        actueljoueur = int(PartieDao.read(id_partie)[0][3])

        if totaljoueur == (actueljoueur+1) :
            partie = Partie(id_partie= id_partie, id_jeu= jeu, temps= 0, statutfin= 1, parampartie= totaljoueur, nbjoueurs= actueljoueur+1, numerotour= 0)
            PartieDao.update(partie)
            ##création ligne participant
            t = len(ParticipantDao.read_all())
            participant = Participant(t+1, id_partie, pseudo, actueljoueur, 1, 0, 0, 0)
            ParticipantDao.create(participant)
            return True
        elif totaljoueur > (actueljoueur+1) :
            partie = Partie(id_partie, jeu, 0, 0, totaljoueur, actueljoueur+1, 0)
            PartieDao.update(partie)
            ##création ligne participant
            t = len(ParticipantDao.read_all())
            participant = Participant(t + 1, id_partie, pseudo, actueljoueur, 1, 0, 0, 0)
            ParticipantDao.create(participant)
            return True
        else:
            return False


    def creer_partie(id_jeu, pseudo, parampartie):

        taille_partie = len(PartieDao.read_all())
        taille_participant = len(ParticipantDao.read_all())

        # créer partie
        partie = Partie(id_partie=taille_partie+1, id_jeu=id_jeu, temps=0, statutfin=0, parampartie=parampartie,
                        nbjoueurs=1, numerotour=1)
        PartieDao.create(partie)

        # créer participant
        participant = Participant(taille_participant+1, taille_partie+1, pseudo, 0, 1, 0, 0, 0)
        ParticipantDao.create(participant)

        return str(taille_partie+1)

    def get_participants(id_partie):

        return ParticipantDao.find_participant(id_partie)


    def get_param(id_partie):

        return PartieDao.read(id_partie)


    # def donner_ordre(id_partie, nvordre, pseudo):
    #
    #     ParticipantDao.update2(id_partie, nvordre, pseudo)
    #     return True
    #
    #
    # def get_id_participant(id_partie, pseudo):
    #
    #     return ParticipantDao.find_id_participant(id_partie, pseudo)
    #
    #
    # def get_all_id_participant(id_partie, pseudo):
    #
    #     return ParticipantDao.find_id_participant_all(id_partie)
    #
    #
    # def creer_pioche(id_partie):
    #
    #     PiocheDao.create(id_partie)
    #     return True
    #
    # def creer_poubelle(id_partie):
    #
    #
    #     PoubelleDao.create(id_partie)
    #     return True


    def donner_ordre(id_partie, nvordre, pseudo):
        nvordre = int(nvordre)
        if nvordre == 1:
            ParticipantDao.update3(id_partie, 1, pseudo)
            ParticipantDao.update2(id_partie, nvordre, pseudo)
        else:
            ParticipantDao.update2(id_partie, nvordre, pseudo)
        return True


    def get_id_participant(id_partie, pseudo):

        return ParticipantDao.find_id_participant(id_partie, pseudo)


    def get_all_id_participant(id_partie):

        return ParticipantDao.find_id_participant_all(id_partie)


    def creer_pioche(id_partie):
        pioche_base = "B200B200B200B200" \
                 "B100B100B100B100B100B100B100B100B100B100B100B100" \
                 "B075B075B075B075B075B075B075B075B075B075" \
                 "B050B050B050B050B050B050B050B050B050B050" \
                 "B025B025B025B025B025B025B025B025B025B025" \
                 "*PRI*CIT*INC*VOL" \
                 "!FEU!FEU!FEU!FEU!FEU" \
                 "!LIM!LIM!LIM!LIM" \
                 "!ESS!ESS!ESS" \
                 "!CRE!CRE!CRE" \
                 "!ACC!ACC!ACC" \
                 "@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU@FEU" \
                 "@LIM@LIM@LIM@LIM@LIM@LIM" \
                 "@ESS@ESS@ESS@ESS@ESS@ESS" \
                 "@ROU@ROU@ROU@ROU@ROU@ROU" \
                 "@REP@REP@REP@REP@REP@REP"
                    # total : 106 cartes

        pioche = Pioche(pioche_base, id_partie)
        paquetmelange = Pioche.melanger(pioche)
        nvpioche = Pioche(paquetmelange, id_partie)
        PiocheDao.create(nvpioche)
        return True


    def creer_poubelle(id_partie):
        poubelle_base = ""
        poub = Poubelle(poubelle_base, id_partie)
        PoubelleDao.create(poub)
        return True

    def creer_main(id_participant):
        L = []
        partie = ParticipantDao.find_id_partie(id_participant)
        mot_pioche = PiocheDao.read_mot(id_participant)
        pioche_base = Pioche(mot_pioche, partie)

        c6 = pioche_base.pioche[0:24]
        m = pioche_base.pioche[24:]
        pioche_reduite = Pioche(m, partie)
        PiocheDao.update(pioche_reduite)

        mano = Main(id_participant, c6)
        MainDao.create(mano)

        return True
        # faire un instance de Main
        # utiliser la méthode pour retourner
        #   ajouter cette liste dans la Dao


    def creer_statut(id_participant):

        stat = [id_participant, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        liste = Statut(stat)
        StatutDao.create(liste)

        return True



    def obtenir_id_particip(id_partie, ordre):

        return ParticipantDao.find_id_participant_ordre(id_partie, ordre)


    def obtenir_pseudo(id_particip):

        return ParticipantDao.find_participant_pseudo(id_particip)


    def obtenir_statut(id_particip):

        return StatutDao.read(id_particip)


    def obtenir_derniere_carte_poubelle(id_partie):

        mot = PoubelleDao.read(id_partie)

        return mot[0:4]


    def obtenir_main(id_participant):

        return MainDao.read(id_participant)


    def obtenir_sontour(id_participant):

        return ParticipantDao.obtenir_sontour(id_participant)


    def piocher_pioche(id_participant, id_partie):

        # prendre la dernière carte de la pioche (0:4)
        paquet = PiocheDao.read_mot(id_participant)
        carte = paquet[0:4]
        # update la pioche
        nvpaquet = paquet[4:]
        PiocheDao.update2(nvpaquet, id_partie)
        # update la main du joueur id_participant
        mano = MainDao.read(id_participant)
        mano = mano + carte
        MainDao.update(mano, id_participant)

        return carte

    def piocher_poubelle(id_participant, id_partie):

        # pioche la derniere carte de la poubelle
        # lire la poubelle
        poub = PoubelleDao.read(id_partie)

        # prendre la dernière carte de la poubelle
        carte = poub[0:4]
        nvpoub = poub[4:]

        # update la poubelle sans la derniere carte
        PoubelleDao.update(nvpoub, id_partie)

        return carte






    def jouer_tour(id_participant, id_partie, carte, target):

        # tester la carte (pleins de if)
            # if c'est possible de jouer cette carte, sur ce joueur, alors on joue (update la main du joueur id_participant, le statut du joueur target)...
            # else : poubelle et zaw update

        id_participant = int(id_participant)
        id_partie = int(id_partie)
        target = int(target)

        statut_target = StatutDao.read2(target)
        poubelle = False


        # bornes

        if carte == "B025":
            if Borne25.peut_on_jouer_25B(statut_target, id_participant) == 1:
                statut_target = Borne25.jouer_25B(statut_target)
            else:
                poubelle = True

        elif carte == "B050":
            if Borne50.peut_on_jouer_50B(statut_target, id_participant) == 1:
                statut_target = Borne50.jouer_50B(statut_target)
            else:
                poubelle = True

        elif carte == "B075":
            if Borne75.peut_on_jouer_75B(statut_target, id_participant) == 1:
                statut_target = Borne75.jouer_75B(statut_target)
            else:
                poubelle = True

        elif carte == "B100":
            if Borne100.peut_on_jouer_100B(statut_target, id_participant) == 1:
                statut_target = Borne100.jouer_100B(statut_target)
            else:
                poubelle = True

        elif carte == "B200":
            if Borne200.peut_on_jouer_200B(statut_target, id_participant) == 1:
                statut_target = Borne200.jouer_200B(statut_target)
            else:
                poubelle = True


        # attaques

        elif carte == "!ACC":
            if accident.peut_on_jouer_accident(statut_target, id_participant) == 1:
                statut_target = accident.jouer_accident(statut_target)
            else:
                poubelle = True

        elif carte == "!CRE":
            if pneucreve.peut_on_jouer_pneucreve(statut_target, id_participant) == 1:
                statut_target = pneucreve.jouer_pneucreve(statut_target)
            else:
                poubelle = True

        elif carte == "!ESS":
            if panne.peut_on_jouer_panne(statut_target, id_participant) == 1:
                statut_target = panne.jouer_panne(statut_target)
            else:
                poubelle = True

        elif carte == "!LIM":
            if limite.peut_on_jouer_limite(statut_target, id_participant) == 1:
                statut_target = limite.jouer_limite(statut_target)
            else:
                poubelle = True

        elif carte == "!FEU":
            if feuRouge.peut_on_jouer_feuRouge(statut_target, id_participant) == 1:
                statut_target = feuRouge.jouer_feuRouge(statut_target)
            else:
                poubelle = True


        # soins

        elif carte == "@REP":
            if reparation.peut_on_jouer_reparation(statut_target, id_participant) == 1:
                statut_target = reparation.jouer_reparation(statut_target)
            else:
                poubelle = True

        elif carte == "@ROU":
            if pneuneuf.peut_on_jouer_pneuneuf(statut_target, id_participant) == 1:
                statut_target = pneuneuf.jouer_pneuneuf(statut_target)
            else:
                poubelle = True

        elif carte == "@ESS":
            if essence.peut_on_jouer_essence(statut_target, id_participant) == 1:
                statut_target = essence.jouer_essence(statut_target)
            else:
                poubelle = True

        elif carte == "@FEU":
            if feuVert.peut_on_jouer_feuVert(statut_target, id_participant) == 1:
                statut_target = feuVert.jouer_feuVert(statut_target)
            else:
                poubelle = True

        elif carte == "@LIM":
            if delimite.peut_on_jouer_delimite(statut_target, id_participant) == 1:
                statut_target = delimite.jouer_delimite(statut_target)
            else:
                poubelle = True


        # joker

        elif carte == "*CIT":
            if joquatari.peut_on_jouer_joquatari(statut_target, id_participant) == 1:
                statut_target = joquatari.jouer_joquatari(statut_target)
            else:
                poubelle = True

        elif carte == "*PRI":
            if calendriercoquin.peut_on_jouer_calendriercoquin(statut_target, id_participant) == 1:
                statut_target = calendriercoquin.jouer_calendriercoquin(statut_target)
            else:
                poubelle = True

        elif carte == "*INC":
            if pneuMichelin.peut_on_jouer_pneuMichelin(statut_target, id_participant) == 1:
                statut_target = pneuMichelin.jouer_pneuMichelin(statut_target)
            else:
                poubelle = True

        elif carte == "*VOL":
            if sebLoeb.peut_on_jouer_sebLoeb(statut_target, id_participant) == 1:
                statut_target = sebLoeb.jouer_sebLoeb(statut_target)
            else:
                poubelle = True

        else :
            print("erreur")



        if poubelle == True:
            poub = PoubelleDao.read(id_partie)
            nvpoub = carte + poub
            PoubelleDao.update(nvpoub, id_partie)


        StatutDao.update(target, statut_target)

        mano = MainDao.read(id_participant)
        nvmano = ''
        i=0

        if len(mano) == 28:
            for j in range(7):
                if mano[4*j : 4*j + 4]!=carte or i==1 :
                    nvmano += str(mano[4*j : 4*j + 4])
                elif mano[4*j : 4*j + 4]==carte:
                    i += 1
            MainDao.update(nvmano, id_participant)

        return ServicePartie.finir_tour(id_participant, id_partie, carte, target)



    def finir_tour(id_participant, id_partie, carte, target):

        # if borne de id_participant >= 1000:
            # return l'id_participant
        bornes_joueur = StatutDao.read2(id_participant)[1]

        if bornes_joueur >= 25:
            # update la partie (statutfin), les participants (classement, enjeu, score), (les stats)
            PartieDao.update2(id_partie, 2)
            ParticipantDao.update4(id_participant, bornes_joueur, 1, 0)
            # peut-être les stats
            # modifier dao stat en fonction de l'id_participant update
            pseudos = ParticipantDao.find_participant(id_partie)
            pseudo = ParticipantDao.find_participant_pseudo(id_participant)
            for i in range(len(pseudos)):
                if pseudos[i][0] == pseudo:
                    stats = StatistiquesDao.read2(pseudos[i][0], 2)
                    nbparties = stats[0][2]
                    nbvictoire = stats[0][0]
                    ratio = (nbvictoire+1) / (nbparties+1)
                    StatistiquesDao.update2(nbvictoire+1, ratio, nbparties+1, pseudos[i][0], 2)
                else:
                    stats = StatistiquesDao.read2(pseudos[i][0], 2)
                    nbparties = stats[0][2]
                    nbvictoire = stats[0][0]
                    ratio = nbvictoire / (nbparties + 1)
                    StatistiquesDao.update2(nbvictoire, ratio, nbparties + 1, pseudos[i][0], 2)

            return 0

        # else :
            # vérifier la pioche pas vide, si elle est vide on prend toute la poubelle, on l'a shuffle 3x et on update la pioche et la poubelle avec le paquet
            # get le numéro de tour de id_partie
            # update le tour (num tour partie +1)
            # modulo pour changer le sontour:
                # update le son tour
            # return le joueur qui doit jouer (ordre)

        else :

            taille_pioche = len(PiocheDao.read_mot(id_participant))

            if taille_pioche < 2 :
                poub = PoubelleDao.read(id_partie)
                L = []
                for i in range(int(len(poub) / 4)):
                    L += [poub[4 * i: 4 * i + 4]]
                random.shuffle(L)
                random.shuffle(L)
                random.shuffle(L)
                nvpoub=""
                paquetmelange = ""
                for i in range(len(L)):
                    paquetmelange += L[i]

                PiocheDao.update2(paquetmelange, id_partie)
                PoubelleDao.update(nvpoub, id_partie)

                # changement de tour #
                # num_tour = int(PartieDao.read2(id_partie))
                # PartieDao.update3(id_partie, num_tour + 1)
                # p = int(PartieDao.read(id_partie)[0][1])
                # a = (num_tour % p)
                # listeparticipants = ParticipantDao.find_id_participant_all(id_partie)
                #
                # for k in range(p):
                #     ordre = int(ParticipantDao.find_ordre(listeparticipants[k][0]))
                #     if a == 0:
                #         # c'est au joueur qui a pour ordre parametre de jouer
                #         if ordre == p:
                #             ParticipantDao.update5(listeparticipants[k][0], 1)
                #         else:
                #             ParticipantDao.update5(listeparticipants[k][0], 0)
                #     else:
                #         # si ton ordre est égal à a c'est à toi de jouer, sinon non
                #         if ordre == a:
                #             ParticipantDao.update5(listeparticipants[k][0], 1)
                #         else:
                #             ParticipantDao.update5(listeparticipants[k][0], 0)



                num_tour = int(PartieDao.read2(id_partie))
                PartieDao.update3(id_partie, num_tour + 1)

                listeparticipants = ParticipantDao.find_id_participant_all(id_partie) # id des participants

                p = int(PartieDao.read(id_partie)[0][1]) # nombre de joueurs dans la partie

                w = ParticipantDao.find_ordre(id_participant)
                z = int(w)+1

                if z > p:
                    for k in range(p):
                        if int(ParticipantDao.find_ordre(listeparticipants[k][0])) == 1:
                            ParticipantDao.update5(listeparticipants[k][0], 1)
                        else :
                            ParticipantDao.update5(listeparticipants[k][0], 0)
                else:
                    for k in range(p):
                        if int(ParticipantDao.find_ordre(listeparticipants[k][0])) == z:
                            ParticipantDao.update5(listeparticipants[k][0], 1)
                        else :
                            ParticipantDao.update5(listeparticipants[k][0], 0)





            else:
                num_tour = int(PartieDao.read2(id_partie))
                PartieDao.update3(id_partie, num_tour + 1)

                listeparticipants = ParticipantDao.find_id_participant_all(id_partie)  # id des participants

                p = int(PartieDao.read(id_partie)[0][1])  # nombre de joueurs dans la partie

                w = ParticipantDao.find_ordre(id_participant)
                z = int(w) + 1

                if z > p:
                    for k in range(p):
                        if int(ParticipantDao.find_ordre(listeparticipants[k][0])) == 1:
                            ParticipantDao.update5(listeparticipants[k][0], 1)
                        else:
                            ParticipantDao.update5(listeparticipants[k][0], 0)
                else:
                    for k in range(p):
                        if int(ParticipantDao.find_ordre(listeparticipants[k][0])) == z:
                            ParticipantDao.update5(listeparticipants[k][0], 1)
                        else:
                            ParticipantDao.update5(listeparticipants[k][0], 0)
                # changement de tour #
                # num_tour = int(PartieDao.read2(id_partie))
                # PartieDao.update3(id_partie, num_tour + 1)
                # p = int(PartieDao.read(id_partie)[0][1])
                # a = (num_tour % p)
                # listeparticipants = ParticipantDao.find_id_participant_all(id_partie)
                #
                # for k in range(p):
                #     ordre = int(ParticipantDao.find_ordre(listeparticipants[k][0]))
                #     if a == 0:
                #         # c'est au joueur qui a pour ordre parametre de jouer
                #         if ordre == p:
                #             ParticipantDao.update5(listeparticipants[k][0], 1)
                #         else:
                #             ParticipantDao.update5(listeparticipants[k][0], 0)
                #     else:
                #         # si ton ordre est égal à a c'est à toi de jouer, sinon non
                #         if ordre == a:
                #             ParticipantDao.update5(listeparticipants[k][0], 1)
                #         else:
                #             ParticipantDao.update5(listeparticipants[k][0], 0)

        return 1





    def obtenir_statutfin(id_partie):

        return int(PartieDao.read(id_partie)[0][2])


    def obtenir_numtour(id_partie):

        return PartieDao.read2(id_partie)
