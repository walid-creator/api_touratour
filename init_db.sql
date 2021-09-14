-------------------- Création des tables --------------------

-- Création de la table "Jeu" --

CREATE TABLE Jeu (
   id_jeu INTEGER,
   nom VARCHAR(40),
   historique TEXT,
   regles TEXT,
   tempsMoyen FLOAT(2)
);

-- Création de la table "Partie" --

CREATE TABLE Partie (
   id_partie INTEGER,
   id_jeu INTEGER,
   temps FLOAT(2),
   statutFin BOOLEAN,
   paramPartie VARCHAR
);

-- Création de la table "Joueur" --

CREATE TABLE Joueur (
   id_joueur INTEGER,
   pseudo VARCHAR(25),
   mdp VARCHAR(58)
);

-- Création de la table "Participant" --

CREATE TABLE Participant (
   id_participant INTEGER,
   id_partie INTEGER,
   pseudo VARCHAR(25),
   ordreParticipant INTEGER,
   enJeu BOOLEAN,
   score INTEGER,
   classementPartie INTEGER 
);

-- Création de la table "Statistiques" --

CREATE TABLE Statistiques (
   id_statistiques INTEGER,
   id_jeu INTEGER,
   pseudo VARCHAR(25),
   nivJeu FLOAT(2),
   classementJeu INTEGER,
   tempsTour FLOAT(2),
   nbPartie INTEGER 
);

-- Création de la table "ParamPartie" --

CREATE TABLE ParamPartie (
   id_paramPartie INTEGER,
   id_jeu INTEGER,
   nomParamPartie VARCHAR
);

-- Création de la table "ValeurPartie" --

CREATE TABLE ValeurPartie (
   id_valeurPartie INTEGER,
   id_paramPartie INTEGER,
   id_partie INTEGER,
   ordreValeurPartie INTEGER,
   valeurpartie VARCHAR
);

-- Création de la table "grille" --

CREATE TABLE grille(
   id_partie INTEGER,
   numcase INTEGER,
   valeur VARCHAR
);

-- Création de la table "Pioche" --

CREATE TABLE Pioche (
    id_partie INTEGER,
    paquet VARCHAR
);

-- Création de la table "Poubelle" --

CREATE TABLE Poubelle (
    id_partie INTEGER,
    paquet VARCHAR
);

-- Création de la table "Main" --

CREATE TABLE Main (
    id_participant INTEGER,
    carte1 VARCHAR
);


-- Création de la table "Statut" --

CREATE TABLE Statut (
    id_participant INTEGER,
    borne INTEGER,
    feu INTEGER,
    limite INTEGER,
    essence INTEGER,
    crevaison INTEGER,
    accident INTEGER,
    botte_pompier INTEGER,
    botte_citerne INTEGER,
    botte_roue INTEGER,
    botte_volant INTEGER 
);



-------------------- Création des clés primaires et étrangères --------------------

-- Clés primaires --

ALTER TABLE Jeu ADD CONSTRAINT pk_id_jeu PRIMARY KEY (id_jeu);

ALTER TABLE Joueur ADD CONSTRAINT pk_pseudo PRIMARY KEY (pseudo);

ALTER TABLE Partie ADD CONSTRAINT pk_id_partie PRIMARY KEY (id_partie);

ALTER TABLE Participant ADD CONSTRAINT pk_id_participant PRIMARY KEY (id_participant);

ALTER TABLE Statistiques ADD CONSTRAINT pk_id_statistiques PRIMARY KEY (id_statistiques);

ALTER TABLE ParamPartie ADD CONSTRAINT pk_id_param_partie PRIMARY KEY (id_paramPartie);

ALTER TABLE ValeurPartie ADD CONSTRAINT pk_id_valeur_partie PRIMARY KEY (id_valeurPartie);

ALTER TABLE Pioche ADD CONSTRAINT pk_id_partie_pioche PRIMARY KEY (id_partie);

ALTER TABLE Poubelle ADD CONSTRAINT pk_id_partie_poubelle PRIMARY KEY (id_partie);

ALTER TABLE Main ADD CONSTRAINT pk_id_participant_main PRIMARY KEY (id_participant);

ALTER TABLE Statut ADD CONSTRAINT pk_id_participant_statut PRIMARY KEY (id_participant);


-- Clés étrangères --

ALTER TABLE Partie ADD CONSTRAINT fk_id_jeu FOREIGN KEY (id_jeu) REFERENCES Jeu (id_jeu);

ALTER TABLE Participant ADD CONSTRAINT fk_pseudo FOREIGN KEY (pseudo) REFERENCES Joueur (pseudo);
ALTER TABLE Participant ADD CONSTRAINT fk_id_partie FOREIGN KEY (id_partie) REFERENCES Partie (id_partie);

ALTER TABLE Statistiques ADD CONSTRAINT fk_pseudo_stat FOREIGN KEY (pseudo) REFERENCES Joueur (pseudo);
ALTER TABLE Statistiques ADD CONSTRAINT fk_id_jeu_stat FOREIGN KEY (id_jeu) REFERENCES Jeu (id_jeu);

ALTER TABLE ParamPartie ADD CONSTRAINT fk_id_jeu_param_partie FOREIGN KEY (id_jeu) REFERENCES Jeu (id_jeu);

ALTER TABLE ValeurPartie ADD CONSTRAINT fk_id_param_partie_valeur_partie FOREIGN KEY (id_paramPartie) REFERENCES ParamPartie (id_paramPartie);
ALTER TABLE ValeurPartie ADD CONSTRAINT fk_id_partie_valeur_partie FOREIGN KEY (id_partie) REFERENCES Partie (id_partie);

ALTER TABLE Pioche ADD CONSTRAINT fk_id_partie_pioche FOREIGN KEY (id_partie) REFERENCES Partie (id_partie);

ALTER TABLE Poubelle ADD CONSTRAINT fk_id_partie_poubelle FOREIGN KEY (id_partie) REFERENCES Partie (id_partie);

ALTER TABLE Main ADD CONSTRAINT fk_id_participant_main FOREIGN KEY (id_participant) REFERENCES Participant (id_participant);

ALTER TABLE Statut ADD CONSTRAINT fk_id_participant_statut FOREIGN KEY (id_participant) REFERENCES Participant (id_participant);

ALTER TABLE grille ADD CONSTRAINT fk_id_partie FOREIGN KEY (id_partie) REFERENCES Partie (id_partie);




-------------------- Insertion de valeurs dans les tables --------------------

INSERT INTO Joueur VALUES (1, 'Axel', '095c7e53e301f6f01819db3816baef60cdccdc7d5c1c51a8cd4a1046'); -- mdp : etiennedao
INSERT INTO Joueur VALUES (2, 'Val', 'a453a4d5c31a291b2792a6bdb7b7c57de529903f8d436efb926cfe83'); -- mdp : onrévolutionnelapoo
INSERT INTO Joueur VALUES (3, 'Célia', '7b68d59fead0065563712ef6618e4dc2aa8a426063e842fa4a1ea73a'); -- mdp : rdv11hvendredi
INSERT INTO Joueur VALUES (4, 'Walid', '3885158bf45542785e1723fd79912065dcd20fe8c01e8c4e941dfad5'); -- mdp : allezlebarça
INSERT INTO Joueur VALUES (5, 'Duvérier', 'f61a05bedc766ce6ed94de41c4025c5e8dffdf5e814f2642d7a21367'); -- mdp : jesuisunverbedu22emegroupe

INSERT INTO parampartie VALUES (1,1,'Langue');
INSERT INTO parampartie VALUES (2,1,'Nbcases');
INSERT INTO parampartie VALUES (3,1,'Pion_j1');
INSERT INTO parampartie VALUES (4,1,'Pion_j2');
INSERT INTO parampartie VALUES (5,1,'Qui_commence');

INSERT INTO Jeu VALUES (1, 'Morpion', 'On trouve une version du morpion dans l empire romain, vers le premier siècle avant notre ère. Le nom Tic Tac Toe
est un mot d origine anglaise. (Source : Yves Guichard)', 'Les joueurs inscrivent tour à tour leur symbole sur une grille qui n a pas de limites ou qui n a que celles du nombre de case fixé. Le premier qui parvient à aligner un nombre déterminé de ses symboles horizontalement, verticalement ou en diagonale gagne un point. Le morpion donne un avantage assez important à celui qui commence. Des formes évoluées existent, comme le Gomoku ou la Pente, qui ajoutent à la notion d alignement une notion de prise. Le renju prévoit des handicaps pour le joueur qui commence, ce qui permet d équilibrer les chances des deux joueurs. (Source : Wikipedia)',0);

INSERT INTO Jeu VALUES (2, '1000 Bornes', 'Les 1000 bornes est un jeu de société utilisant des cartes spéciales sur le thème de la course automobile à ses débuts. Il a été inventé en 1954 par Edmond Dujardin, un éditeur de matériel pour auto-écoles, illustré par Joseph Le Callennec, graphiste et appartient actuellement à TF1 Games. Historiquement, le jeu s inspire de Touring, un jeu de cartes américain créé en 19061 Chaque année, il est vendu à des centaines de milliers d exemplaires dans le monde. Sur les premières boîtes du jeu, il était sous-titré : La canasta de la route. Le nom du jeu vient des bornes kilométriques jalonnant le réseau routier français et de la longueur de la mythique et ancienne Route nationale 7, en France, qui fait environ 1 000 km (996 km exactement). Depuis 2009, la fabrication se fait à l usine située à Saint-Pantaléon-de-Larche en Corrèze. (Source : Wikipedia)', 'Lorsque c’est votre tour, piochez une carte.
Vous avez maintenant 7 cartes en main et 6 possibilités :
1. Si vous avez un Feu Vert, vous pouvez démarrer votre course.
Pour cela, posez votre carte Feu Vert devant vous.
Précision : la carte Feu Vert est très importante car c’est la première
carte que vous devez jouer avant de pouvoir démarrer la course.
2. Si vous avez une carte Borne ET que vous avez déjà devant vous une
carte Feu Vert ou la botte Véhicule Prioritaire, vous pouvez poser votre
carte Borne, et ainsi avancer dans la course !
3. Si vous avez une carte Attaque, vous pouvez la poser sur le jeu de l’un de
vos adversaires pour le retarder dans sa course, à condition que celui-ci
ait devant lui une carte Feu Vert sur le dessus de sa pile de Bataille (ou la
botte Véhicule Prioritaire). La Limite de Vitesse est la seule carte Attaque
que vous pouvez placer devant un adversaire qui n’a pas encore démarré.
Précision : vous pouvez attaquer un adversaire même si vous êtes vousmême déjà attaqué ou que vous n’avez pas encore démarré.
4. Si vous avez subi une attaque lors du tour précédent, vous pouvez stopper cette attaque en posant par-dessus la carte Parade correspondante.
Précision : vous n’avez pas besoin de poser un Feu Vert pour pouvoir
redémarrer. La carte Parade suffi t pour poursuivre votre course.
5. Si vous avez une Botte, vous pouvez la poser devant vous. Elle sert
d’immunité contre une attaque bien précise.
Précision : le fait de poser une Botte vous donne le droit de rejouer
immédiatement. Piochez alors une autre carte et rejouez.
6. Si vous ne pouvez jouer aucune carte sur votre Zone de Jeu ou sur
celles de vos adversaires, jetez une de vos cartes dans la défausse.
Il vous reste de nouveau 6 cartes en main. Votre tour de jeu est terminé
et c’est maintenant à votre voisin de gauche de jouer.
Le jeu continue ainsi jusqu’à ce que l’un d’entre vous totalise EXACTEMENT
1 000 Bornes avec les cartes Bornes posées devant lui, ou bien dès qu’il n’y
a plus de carte Bornes dans le sabot.
Précision : si personne n’atteint 1 000 Bornes, le joueur qui gagne est celui
qui en est le plus proche, sans les dépasser. (Source : Dujardin Jeux)',0);
