from flask import Flask, request
from serveur.service.servicestat import ServiceStat
from serveur.service.service import Service_Tache
from serveur.service.service_classement import Service_Classement
from serveur.service.service_creer_compte import ServiceCreerCompte
from serveur.service.service_connexion import ServiceConnexion
from serveur.service.service_modifier_mdp import ServiceModifierMdp
from serveur.service.service_partie import ServicePartie
from serveur.service.service_param import ServiceParam
from serveur.service.service_grille import ServiceGrille
from serveur.service.service_case import ServiceCase
from serveur.service.service_langue import ServiceLangue
from serveur.service.service_pion import ServicePion
from serveur.service.service_modif_tour import ServiceModifTour
import json
from serveur.service.service_premier import ServicePremier

def retour(code, message):
    return {"code": code, "message": message}


# def controleDonneesCreationTache(dic):
#     message = ""
#     if dic is None:
#         message = "Aucun paramètre données"
#     if type(dic) != dict or not ("nom" in dic.keys()) or not ("details" in dic.keys()):
#         message = 'Json attendu de la forme : {"nom":"...","details":"...."}'
#     return message



app = Flask(__name__)

# Afficher la liste des jeux
@app.route('/jeux', methods=["GET"])
def listeJeux():
    #racine = "http://127.0.0.2:5000/jeux/"
    liste = Service_Tache.retrouveTousLesNoms()
    return json.dumps(liste)

# Afficher le classement du Morpion
@app.route('/statistiques/Morpion', methods=["GET"])
def classementM():
    liste = Service_Classement.retrouveStatsMorpion()
    return json.dumps(liste)

# Afficher le classement du 1000 Bornes
@app.route('/statistiques/1000Bornes', methods=["GET"])
def classementB():
    liste = Service_Classement.retrouveStats1000B()
    return json.dumps(liste)


# Afficher les statistiques d'un joueur
@app.route('/statistiques/<pseudo>', methods=["POST"])
def stat(pseudo):
    dic = request.get_json()
    pseudo = dic["pseudo"]
    liste = ServiceStat.stats_joueur(pseudo)
    return json.dumps(liste)

# Tester si le pseudo est dans la base de données ou non
@app.route('/joueurs/tester_pseudo/<pseudo>', methods=["POST"])
def verifPseudo(pseudo):
    dic = request.get_json()
    pseudo = dic["pseudo"]
    try:
        if ServiceCreerCompte.verifSiDejaPseudo(pseudo) == 0:
            return retour("401", "Pas OK"), 401
        elif ServiceCreerCompte.verifSiDejaPseudo(pseudo) == 1:
            return retour("402", "Pas OK"), 402
        elif ServiceCreerCompte.verifSiDejaPseudo(pseudo) == 2:
            return retour("200", "OK"), 200
        else:
            return retour("500", "Pas OK"), 500
    except Exception:
        return retour("500", "Pas OK"), 500

# Créer un joueur
@app.route('/joueurs/creer_joueur/<pseudo>', methods=["POST"])
def creerJoueur(pseudo):
    dic = request.get_json()
    pseudo = dic["pseudo"]
    mdp = dic["mdp"]
    try:
        if ServiceCreerCompte.verifMdp(pseudo, mdp) == 1:
            return retour("201", "OK"), 200
        else:
            return retour("401", "OK"), 401
    except Exception:
        return retour("500", "Pas OK"), 500

# Connecter un joueur
@app.route('/joueurs/connexion/<pseudo>', methods=["POST"])
def connexionJoueur(pseudo):
    dic = request.get_json()
    pseudo = dic["pseudo"]
    mdp = dic["mdp"]
    try:
        if ServiceConnexion.se_connecter(pseudo, mdp)==True:
            return retour("200", "L'indentification est valide"), 200
        else:
            return retour("401", "Identification échouée"), 401
    except Exception:
        return retour("500", "Identification échouée"), 500


# Modifier un pseudo
@app.route('/joueurs/modification/<pseudo>', methods=["PUT"])
def modifierMdp(pseudo):
    dic = request.get_json()
    pseudo = dic["pseudo"]
    mdp = dic["mdp"]
    try:
        if ServiceModifierMdp.modifMdp(pseudo, mdp)==2:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


# Obtenir les parties en attente
@app.route('/parties/en_attente/<jeu>', methods=["POST"])
def obtenirParties(jeu):
    dic = request.get_json()
    jeu = dic["jeu"]
    liste = ServicePartie.obtenir_parties(jeu)
    return json.dumps(liste)

# Obtenir les parties en attente
@app.route('/parties/participants/<id_partie>', methods=["POST"])
def obtenirParticipants(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    liste = ServicePartie.get_participants(id_partie)
    return json.dumps(liste)

# Obtenir les parties en attente
@app.route('/parties/param/<id_partie>', methods=["POST"])
def obtenirParam(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    liste = ServicePartie.get_param(id_partie)
    return json.dumps(liste)


# Choisir les parties en attente
@app.route('/parties/rejoindre/<pseudo>', methods=["POST"])
def choisirPartie(pseudo):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    jeu = dic["jeu"]
    pseudo = dic["pseudo"]
    try:
        if ServicePartie.choisir_partie(id_partie, jeu, pseudo) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


# Creer une partie
@app.route('/parties/creer_partie/<pseudo>', methods=["POST"])
def creerPartie(pseudo):
    dic = request.get_json()
    parampartie = dic["parampartie"]
    id_jeu = dic["id_jeu"]
    pseudo = dic["pseudo"]
    liste = ServicePartie.creer_partie(id_jeu, pseudo, parampartie)
    return json.dumps(liste)


# Creer les parametres
@app.route('/parametres/creer_param/<id_partie>', methods=["POST"])
def creerParam(id_partie):
    dic = request.get_json()
    valeur = dic["valeurparam"]
    id_partie = dic["id_partie"]
    try:
        if ServiceParam.creer_param(id_partie,valeur) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


# # Changer les ordres de tour
# @app.route('/parties/ordre/<id_partie>/<pseudo>', methods=["POST"])
# def donnerOrdre(id_partie, pseudo):
#     dic = request.get_json()
#     pseudo = dic["pseudo"]
#     id_partie = dic["id_partie"]
#     nvordre = dic["nvordre"]
#     try:
#         if ServicePartie.donner_ordre(id_partie, nvordre, pseudo) == True :
#             return retour("200", "La modification est valide"), 200
#         else:
#             return retour("401", "modification échouée"), 401
#     except Exception:
#         return retour("500", "modification échouée"), 500

#
# @app.route('/parties/get_id_participant/<id_partie>/<pseudo>', methods=["POST"])
# def getIdParticipant(id_partie, pseudo):
#     dic = request.get_json()
#     id_partie = dic["id_partie"]
#     pseudo = dic["pseudo"]
#     liste = ServicePartie.get_id_participant(id_partie, pseudo)
#     return json.dumps(liste)
#
# @app.route('/parties/get_all_id_participant/<id_partie>/', methods=["POST"])
# def getAllIdParticipant(id_partie):
#     dic = request.get_json()
#     id_partie = dic["id_partie"]
#     liste = ServicePartie.get_all_id_participant(id_partie)
#     return json.dumps(liste)
#
# # Changer les ordres de tour
# @app.route('/parties/creer_pioche/<id_partie>', methods=["POST"])
# def creerPioche(id_partie):
#     dic = request.get_json()
#     id_partie = dic["id_partie"]
#     try:
#         if ServicePartie.creer_pioche(id_partie) == True :
#             return retour("200", "La modification est valide"), 200
#         else:
#             return retour("401", "modification échouée"), 401
#     except Exception:
#         return retour("500", "modification échouée"), 500
#
# # Changer les ordres de tour
# @app.route('/parties/creer_poubelle/<id_partie>', methods=["POST"])
# def creerPoubelle(id_partie):
#     dic = request.get_json()
#     id_partie = dic["id_partie"]
#     try:
#         if ServicePartie.creer_poubelle(id_partie) == True :
#             return retour("200", "La modification est valide"), 200
#         else:
#             return retour("401", "modification échouée"), 401
#     except Exception:
#         return retour("500", "modification échouée"), 500




# Changer les ordres de tour
@app.route('/parties/ordre/<id_partie>/<pseudo>', methods=["POST"])
def donnerOrdre(id_partie, pseudo):
    dic = request.get_json()
    pseudo = dic["pseudo"]
    id_partie = dic["id_partie"]
    nvordre = dic["nvordre"]
    try:
        if ServicePartie.donner_ordre(id_partie, nvordre, pseudo) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


@app.route('/parties/get_id_participant/<id_partie>/<pseudo>', methods=["POST"])
def getIdParticipant(id_partie, pseudo):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    pseudo = dic["pseudo"]
    liste = ServicePartie.get_id_participant(id_partie, pseudo)
    return json.dumps(liste)

@app.route('/parties/get_all_id_participant/<id_partie>', methods=["POST"])
def getAllIdParticipant(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    liste = ServicePartie.get_all_id_participant(id_partie)
    return json.dumps(liste)

# Changer les ordres de tour
@app.route('/parties/creer_pioche/<id_partie>', methods=["POST"])
def creerPioche(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    try:
        if ServicePartie.creer_pioche(id_partie) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500

# Changer les ordres de tour
@app.route('/parties/creer_poubelle/<id_partie>', methods=["POST"])
def creerPoubelle(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    try:
        if ServicePartie.creer_poubelle(id_partie) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


# # Changer les ordres de tour
# @app.route('/parties/creer_main/<id_participant>', methods=["POST"])
# def creerMain(id_participant):
#     dic = request.get_json()
#     id_participant = dic["id_participant"]
#     try:
#         if ServicePartie.creer_main(id_participant) == True :
#             return retour("200", "La modification est valide"), 200
#         else:
#             return retour("401", "modification échouée"), 401
#     except Exception:
#         return retour("500", "modification échouée"), 500
#
#
# # Changer les ordres de tour
# @app.route('/parties/creer_statut/<id_participant>', methods=["POST"])
# def creerStatut(id_participant):
#     dic = request.get_json()
#     id_participant = dic["id_participant"]
#     try:
#         if ServicePartie.creer_statut(id_participant) == True :
#             return retour("200", "La modification est valide"), 200
#         else:
#             return retour("401", "modification échouée"), 401
#     except Exception:
#         return retour("500", "modification échouée"), 500

@app.route('/parties/creer_main/<id_participant>', methods=["POST"])
def creerMain(id_participant):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    try:
        if ServicePartie.creer_main(id_participant) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


# Changer les ordres de tour
@app.route('/parties/creer_statut/<id_participant>', methods=["POST"])
def creerStatut(id_participant):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    try:
        if ServicePartie.creer_statut(id_participant) == True :
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500




@app.route('/parties/obtenir_id_particip/<id_partie>/<ordre>', methods=["POST"])
def obtenir_id_particip(id_partie, ordre):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    ordre = dic["ordre"]
    liste = ServicePartie.obtenir_id_particip(id_partie, ordre)
    return json.dumps(liste)

@app.route('/parties/obtenir_pseudo/<id_particip>', methods=["POST"])
def obtenir_pseudo(id_particip):
    dic = request.get_json()
    id_particip = dic["id_participant"]
    liste = ServicePartie.obtenir_pseudo(id_particip)
    return json.dumps(liste)

@app.route('/parties/obtenir_statut/<id_particip>', methods=["POST"])
def obtenir_statut(id_particip):
    dic = request.get_json()
    id_particip = dic["id_participant"]
    liste = ServicePartie.obtenir_statut(id_particip)
    return json.dumps(liste)

@app.route('/parties/obtenir_derniere_carte_poubelle/<id_partie>', methods=["POST"])
def obtenir_derniere_carte_poubelle(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    liste = ServicePartie.obtenir_derniere_carte_poubelle(id_partie)
    return json.dumps(liste)

@app.route('/parties/obtenir_main/<id_participant>', methods=["POST"])
def obtenir_main(id_participant):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    liste = ServicePartie.obtenir_main(id_participant)
    return json.dumps(liste)

@app.route('/parties/obtenir_sontour/<id_participant>', methods=["POST"])
def obtenir_sontour(id_participant):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    liste = ServicePartie.obtenir_sontour(id_participant)
    return json.dumps(liste)



@app.route('/parties/piocher_pioche/<id_participant>/<id_partie>', methods=["POST"])
def piocher_pioche(id_participant, id_partie):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    id_partie = dic["id_partie"]
    liste = ServicePartie.piocher_pioche(id_participant, id_partie)
    return json.dumps(liste)


@app.route('/parties/piocher_poubelle/<id_participant>/<id_partie>', methods=["POST"])
def piocher_poubelle(id_participant, id_partie):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    id_partie = dic["id_partie"]
    liste = ServicePartie.piocher_poubelle(id_participant, id_partie)
    return json.dumps(liste)

# recup grille
@app.route('/jeux/morpion/recuperation_grille/<id_partie>', methods=["POST"])
def recupererGrille(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    nb_cases = dic["nb_cases"]
    liste = ServiceGrille.recuperer(id_partie,nb_cases)
    return json.dumps(liste)

@app.route('/parties/jouer_tour/<id_participant>/<id_partie>/<carte>/<target>', methods=["POST"])
def jouer_tour(id_participant, id_partie, carte, target):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    id_partie = dic["id_partie"]
    carte = dic["carte"]
    target = dic["target"]
    try:
        if ServicePartie.jouer_tour(id_participant, id_partie, carte, target) == 1:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 201
    except Exception:
        return retour("500", "modification échouée"), 500

# @app.route('/parties/jouer_tour/<id_participant>/<id_partie>/<carte>/<target>', methods=["POST"])
# def jouer_tour(id_participant, id_partie, carte, target):
#     dic = request.get_json()
#     id_participant = dic["id_participant"]
#     id_partie = dic["id_partie"]
#     carte = dic["carte"]
#     target = dic["target"]
#     try:
#         if ServicePartie.jouer_tour(id_participant, id_partie, carte, target) == 1:
#             return retour("200", "La modification est valide"), 200
#         else:
#             return retour("401", "modification échouée"), 201
#     except Exception:
#         return retour("500", "modification échouée"), 500


@app.route('/parties/obtenir_statutfin/<id_partie>', methods=["POST"])
def obtenir_statutfin(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    try:
        if ServicePartie.obtenir_statutfin(id_partie) == 2:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 201
    except Exception:
        return retour("500", "modification échouée"), 500

# recup le nb de cases
@app.route('/recup_nbcase/<id_partie>', methods=["POST"])
def recup_cases(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    liste = ServiceCase.recup_nbcases(id_partie)
    return json.dumps(liste)

# recup la langue
@app.route('/recup_langue/<choix>', methods=["POST"])
def recup_langue(choix):
    dic = request.get_json()
    choix = dic["choix"]
    liste = ServiceLangue.recup_langue(choix)
    return json.dumps(liste)


@app.route('/jeux/morpion/recup_param/<id_participant>/<nomParam>, methods=["POST"]')
def recupererparam(id_participant,nomParam):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    nomParam = dic["nomParam"]
    liste = ServiceGrille.recupererparam(id_participant,nomParam)
    return json.dumps(liste)


@app.route('/parties/obtenir_numtour/<id_partie>', methods=["POST"])
def obtenir_numtour(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    liste = ServicePartie.obtenir_numtour(id_partie)
    return json.dumps(liste)


# recup pion
@app.route('/recup_pion/<choix>', methods=["POST"])
def recup_pion(choix):
    dic = request.get_json()
    choix = dic["choix"]
    liste = ServicePion.recup_pion(choix)
    return json.dumps(liste)


# recup premier
@app.route('/recup_premier/<choix>', methods=["POST"])
def recup_premier(choix):
    dic = request.get_json()
    choix = dic["choix"]
    liste = ServicePremier.recup_premier(choix)
    return json.dumps(liste)



# def modifierGrille(numcase, valeur):

@app.route('/jeux/morpion/modification/<id_partie>/<numcase>/<valeur>', methods=["POST"])
def modifierGrille(id_partie,numcase, valeur):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    numcase = dic["numcase"]
    valeur = dic["valeur"]
    try:
        if ServiceGrille.modifier(id_partie,numcase, valeur)==1:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


@app.route("/jeux/morpion/grille/pleine/<id_partie>", methods=["POST"])
def grillepleine(id_partie):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    try:
        if ServiceGrille.pleine(id_partie) == 1:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500

@app.route("/jeux/morpion/grille/aligne/<id_partie>/<pion>", methods=["POST"])
def alignergrille(id_partie,pion):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    pion = dic["pion"]
    try:
        if ServiceGrille.aligner(id_partie,pion) == 1:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500



@app.route("/modifier_mon_tour/<id_participant>/<tour>", methods=["PUT"])
def modif_tour(id_participant,tour):
    dic = request.get_json()
    id_participant = dic["id_participant"]
    tour = dic["tour"]
    try:
        if ServiceModifTour.modif_tour(id_participant,tour) == 0:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500


# Obtenir les parties en attente
@app.route('/parties/en_attenteM/<jeu>', methods=["POST"])
def obtenirPartiesM(jeu):
    dic = request.get_json()
    jeu = dic["jeu"]
    liste = ServicePartie.obtenir_partiesM(jeu)
    return json.dumps(liste)

@app.route("/jeux/morpion/grille/verif_case/<id_partie>/<numcase>", methods=["POST"])
def verifcase(id_partie,numcase):
    dic = request.get_json()
    id_partie = dic["id_partie"]
    numcase = dic["numcase"]
    try:
        if ServiceGrille.verif_case(id_partie,numcase) == 1:
            return retour("200", "La modification est valide"), 200
        else:
            return retour("401", "modification échouée"), 401
    except Exception:
        return retour("500", "modification échouée"), 500

# recup pion
@app.route('/recup_pion/<choix>', methods=["POST"])
def recup_pion1(choix):
    dic = request.get_json()
    choix = dic["choix"]
    liste = ServicePion.recup_pion1(choix)
    return json.dumps(liste)





app.run(debug=True,host="127.0.0.4", port=5000, use_reloader=False)  # run app in debug mode on port 5000