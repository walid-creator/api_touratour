from __future__ import division

import threading
import time
import random

##############################################################################
# Mise en place de la grille du jeu
imax = 3
jmax = 3
grille = []
for i in range(0, imax):
    grille.append([])
    for j in range(0, jmax):
        grille[i].append(' ')

#grille=[['','O', 'O'],
        #['', 'X', 'X'],
        #['', '', '']]
print(grille)


def grillepleine():
    global grille, imax, jmax
    for i in range(0, imax):
        for j in range(0, jmax):
            if grille[i][j] == ' ':
                return False
    return True


###############################################################################
def jeugagne():
    def _jeugagne(pion):
        global grille
        x = pion + pion + pion
        if \
                grille[0] == x or \
                        grille[1] == x or \
                        grille[2] == x or \
                        grille[0][0] + grille[1][0] + grille[2][0] == x or \
                        grille[0][1] + grille[1][1] + grille[2][1] == x or \
                        grille[0][2] + grille[1][2] + grille[2][2] == x or \
                        grille[0][0] + grille[1][1] + grille[2][2] == x or \
                        grille[0][2] + grille[1][1] + grille[2][0] == x:
            return True
        else:
            return False

    if _jeugagne('X'):
        return 'X'
    if _jeugagne('O'):
        return 'O'
    return ''

##########################################################################################################################
class JoueurMorpion(threading.Thread):

    def __init__(self, nom, num, pion):
        threading.Thread.__init__(self)
        self.setName(nom)  # nom du joueur. Ex: "joueur1", "joueur2", ...
        self.num = num  # numÈro du joueur. Ex: 0 pour joueur1, 1 pour joueur2, etc...
        self.pion = pion  # forme de pion affectÈ
        '''self.typejoueur = typejoueur  # type de joueur: 0 = ordinateur, 1 = humain'''
        self.stop = False  # drapeau pour stopper le thread ‡ la demande du programme principal

    def run(self):
        # accËs aux variables globales
        global verrou  # verrou d'accËs aux variables globales
        global okjoue  # drapeau donnÈe par le programme principal qui permet au joueur de jouer
        global cdcoups  # compteur de coups
        global premier  # dÈsigne le numÈro du joueur qui a jouÈ en premier
        global nbjoueurs  # nombre de joueurs du jeu
        '''global aide  # dit si l'affichage d'une aide est demandÈ'''

        while not self.stop:  # tant que le jeu n'est pas terminÈ

            ##### => chaque joueur attend son tour pour jouer
            while True:
                # on prend le verrou d'accËs aux variables globales
                verrou.acquire()
                if self.stop:
                    # jeu terminÈ. on sort de la boucle, mais en conservant le blocage du verrou
                    break
                if okjoue and (cdcoups + premier) % nbjoueurs == self.num:
                    # = Áa y est, on peut jouer, mais on conserve le verrou jusqu'‡ la fin du coup
                    break
                # AprËs la fin du coup, on libËre le verrou pour que les autres joueurs accÈdent aussi aux variables globales
                verrou.release()

            ##### => le joueur en cours joue

            if not self.stop:
                # c'est un joueur "humain" qui joue
                if self.pion == 'X':
                        pionautre = 'O'
                else:
                        pionautre = 'X'
                print(self.getName() + " joue ('" + self.pion + "' contre '" + pionautre + "')")
                ch = self.getName() + " joue case (ligne,colonne):"
                while True:
                    self.coup = input(ch)
                    try:
                        # ici, le joueur a entrÈ un choix ligne,colonne
                        x = eval(self.coup)
                        if ((type(x) == list or type(x) == tuple) and len(x) == 2) \
                                and (x[0] in [0, 1, 2]) and (x[1] in [0, 1, 2]) \
                                and grille[x[0]][x[1]] == ' ':
                            grille[x[0]][x[1]] = self.pion
                            break
                    except:
                        pass

                        # ici, le choix entrÈ n'est pas correct


            ##### => fin du coup du joueur en cours

            # le joueur repasse la main au programme principal aprËs chaque coup
            okjoue = False
            # on libËre le verrou d'accËs aux variables globales
            verrou.release()
            # et fin du thread si c'est demandÈ (sinon, attente du prochain coup)
            if self.stop:
                break

    def stopper(self):
        self.stop = True


###############################################################################

print("Bonjour! En route pour le jeu de morpion!")

############################## => initialisation du jeu et des conditions de son dÈmarrage
############################## => initialisation du jeu et des conditions de son dÈmarrage

# nombre de joueurs
nbjoueurs = 2

# type de joueurs: 0=ordinateur, 1=humain; on doit avoir: len(typejoueurs)==nbjoueurs


# type de pion affectÈ ‡ chaque joueur.
pions = ['O', 'X']  #
print(u"=====> le joueur1 a le pion 'O', et l'autre le pion 'X'")

# dÈfinir celui qui commence, ou dÈfinir au hasard
while True:
    print(u"DÈfinir qui va commencer")
    print(u"[1] le joueur 1 commence")
    print(u"[2] le joueur 2 commence")
    print(u"[3] le joueur qui commence est dÈfini au hasard")
    x = input(u"Quel choix voulez-vous? [3 par defaut]: ")
    if x == '1':
        premier = 0
        break
    elif x == '2':
        premier = 1
        break
    elif x == '3' or x == '':
        premier = random.randint(0, nbjoueurs - 1)
        break

print("=====> c'est joueur" + str(premier + 1) + " qui commence")

############################## => initialisation du programme

# crÈation du verrou qui permettra le monopole d'accËs aux variables globales (lecture-Ècriture)
verrou = threading.Lock()

# crÈation du "compteur de coups" initialisÈ ‡ -1 parce que c'est le programme principal qui commence
cdcoups = -1

# drapeau initialisÈ ‡ True pour que le programme principal reprenne la main aprËs chaque coup
#   (initialisÈ ‡ -1 parce que c'est le programme principal qui commence)
okjoue = False

# creation de la liste des joueurs (NB: le joueur numÈro 0 est appelÈ "joueur1")
joueurs = []
for i in range(0, nbjoueurs):
    j = JoueurMorpion("joueur%d" % (i + 1), i, pions[i])
    j.setDaemon(True)
    joueurs.append(j)

# lancement de tous les threads des joueurs
for i in range(0, nbjoueurs):
    joueurs[i].start()

##############################
# surveillance du jeu et attente condition de fin de partie

tps = time.time()
while True:
    # attente qu'un joueur ait jouÈ
    while True:
        verrou.acquire()
        if not okjoue:
            cdcoups += 1  # on incrÈmente le compteur de coups du coup qui vient d'Ítre jouÈ
            # on sort de la boucle, mais le verrou reste bloquÈ pendant la surveillance
            break
        verrou.release()

    # affichage de la grille aprËs le dernier coup
    for i in range(0, imax):
        print(grille[i])

    # voir si un gagnant
    x = jeugagne()
    if x != "":
        if x == pions[0]:
            gagnant = "joueur1 ('" + pions[0] + "')"
        else:
            gagnant = "joueur2 ('" + pions[1] + "')"
        print("le gagnant est: " + gagnant)
        verrou.release()
        break

    # condition de fin de jeu
    if grillepleine():
        print("pas de gagnant!")
        verrou.release()
        break

    # dÈtection du dÈpart d'un nouveau tour numÈro ((cdcoups//nbjoueurs)+1) par (cdcoups%nbjoueurs==0)
    ch = ""
    if cdcoups % nbjoueurs == 0:
        print(u"=====> dÈbut du tour " + str((cdcoups // nbjoueurs) + 1))

    # permet au joueur suivant de jouer
    okjoue = True
    verrou.release()
    # et on boucle pour attendre jusqu'‡ ce que le joueur suivant ait jouÈ

#############################
# fin du jeu
print("fin du jeu")

# arrÍt de tous les threads
for i in range(0, nbjoueurs):
    joueurs[i].stopper()

# attente jusqu'‡ ce que tous les threads soient terminÈs
for i in range(0, nbjoueurs):
    joueurs[i].join()
    verrou.acquire()
    print("fin du thread " + joueurs[i].getName())
    verrou.release()

print(u"A bientÙt pour un prochain jeu!")
