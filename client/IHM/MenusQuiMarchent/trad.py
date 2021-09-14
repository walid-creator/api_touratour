#Menu choix parametres
cases = ["Avec quel nombre de cases voulez-vous jouer (9, 16 ou 25) ? ",
         "¿Con cuántas casillas quieres jugar (9, 16 o 25)? ",
         "Con quante caselle vuoi giocare (9, 16 o 25)? ",
         "How many squares do you want to play with (9, 16 or 25)? ",
         "Su kiek kvadrat norite aisti (9, 16 ar 25)? ",
         "Met hoeveel vierkanten wil je spelen (9, 16 of 25)?"]
rpcases = ["Veuillez ressaisir avec quel nombre de cases voulez-vous jouer (9, 16 ou 25) ",
           "Por favor, vuelva a introducir el número de casillas con las que quiere jugar (9, 16 o 25) ",
           "Si prega di inserire nuovamente il numero di caselle con cui si vuole giocare (9, 16 o 25)",
           "Please re-enter the number of squares you want to play with (9, 16, or 25)",
           "veskite dar kart su kiek kvadrat norite aisti (9, 16 ar 25)",
           "Voer opnieuw in met hoeveel vakjes je wilt spelen (9, 16 of 25)"]
p1 = ["Veuillez saisir le pion que vous voulez :", "Por favor, introduzca el peón que desee:",
      "Inserisci il pedone che vuoi:",
      "Please enter the pawn you want:", "veskite norim pstinink:", "Voer de gewenste pion in:"]
p2 = ["Veuillez saisir le pion de votre adversaire : ", "Por favor, introduzca el peón de su oponente: ",
      "Inserisci il pedone del tuo avversario: ",
      "Please enter your opponent's pawn: ", "veskite prieininko pstinink:",
      "Voer de pion van je tegenstander in:"]
ep2 = ["Erreur, veuillez resaisir le pion de votre adversaire : ",
       "Error, por favor vuelva a entrar en el peón de su oponente: ",
       "Errore, per favore, reinserisci il pedone del tuo avversario: ",
       "Error, please re-enter your opponent's pawn: ",
       "Klaida, praau i naujo vesti prieininko pstinink:",
       "Fout, voer de pion van je tegenstander opnieuw in:"]
begin = ["Définir qui va commencer", "Definir quién va a empezar", "Definire chi inizierà",
         "Define who will start", "Apibrkite, kas prads", "Definieer wie er zal beginnen"]
beginj1 = ["[1] le joueur 1 commence", "[1] el jugador 1 comienza", "[1] il giocatore 1 inizia",
           "[1] player 1 starts", "[1] startuoja 1 aidjas", "[1] speler 1 begint"]
beginj2 = ["[2] le joueur 2 commence", "[2] el jugador 2 comienza", "[2] il giocatore 2 inizia",
           "[2] player 2 starts", "[2] startuoja 2 aidjas", "[2] speler 2 begint"]
beginrandom = ["[3] le joueur qui commence est défini au hasard",
               "[3] el jugador inicial está definido al azar",
               "[3] il giocatore titolare è definito in modo casuale",
               "[3] the starting player is set at random",
               "[3] startuojantis aidjas apibriamas atsitiktinai",
               "[3] de startspeler is willekeurig gedefinieerd"]
choicex = ["Quel choix voulez-vous? [3 par defaut]: ", "¿Qué opción quieres? [3 por defecto]:",
           "Quale scelta vuoi? [3 per impostazione predefinita]:",
           "What choice do you want? [3 by default]: ",
           "Kokio pasirinkimo norite? [3 pagal numatytuosius nustatymus]: ",
           "Welke keuze wil je? [3 standaard]: "]

# Menu attente
ljoueur=["Voici la liste des joueurs ayant déjà rejoint la partie","Aquí está la lista de jugadores que ya se han unido al juego",
         "Ecco l'elenco dei giocatori che hanno già aderito al gioco","Here is the list of players who have already joined the game",
         "ia yra aidj, kurie jau prisijung prie aidimo, sraas","Hier is de lijst met spelers die al meedoen aan het spel"]
att=["Nous attendons encore la venue de ","Todavía estamos esperando a ","Stiamo ancora aspettando ",
     "We are still waiting for the arrival of ","Mes vis dar laukiame, kol atvyks ","We wachten nog op de komst van "]
joueur=[" joueur"," jugador"," giocatore"," player"," aidjas"," speler"]
pat=["La partie va commencer, veuillez patienter ...","El juego está a punto de comenzar, por favor espere...",
     "Il gioco sta per iniziare, per favore aspetta...","The game is about to start, please wait ...",
     "aidimas prasids, palaukite ...","Het spel wordt gestart, een ogenblik geduld ..."]

# Menu Tour à Tour
tour=["A votre tour, que voulez-vous faire ?","Ahora es tu turno, ¿qué quieres hacer?","Ora tocca a te, cosa vuoi fare?",
      "Now it's your turn, what do you want to do?","K norite padaryti savo ruotu?","Nu is het jouw beurt, wat wil je doen?"]
o1=["Jouer","Juega","Gioca","To play","aisti","Speel"]
o2=["Abandonner","Abandona","Abbandona","To abandon","Atsisakyk aidimo","Verlaat"]
rep=["\n saisissez votre réponse : ","\n introduzca su respuesta: ","\n inserisci la tua risposta : ",
     "\n enter your answer :","\n veskite savo atsakym: ","\n voer uw antwoord in: "]
err=["La valeur attendue doit être un entier","El valor esperado debe ser un número entero","Il valore atteso deve essere un numero intero",
     "The expected value must be an integer","Laukiama vert turi bti sveikasis skaiius","De verwachte waarde moet een geheel getal zijn"]
joke=["Petit blagueur","Pequeño bromista","Piccolo jolly","Little joker","Maas juokdarys","Kleine grapjas"]
att2=["veuillez attendre votre tour","por favor, espere su turno","si prega di attendere il vostro turno",
     "please wait your turn","praau palaukti savo eils","wacht alstublieft op uw beurt"]
num=["donner le numéro de la case (entre 0 et {}) : ","dar el número de la caja (entre 0 y {}) : ","indicare il numero della casella (tra 0 e {}) : ",
     "give the number of the box (between 0 and {}) : ","nurodykite laukelio numer (nuo 0 iki {}) : ","geef het nummer van het vak (tussen 0 en {}) : "]
verif=["La case est déjà jouée, veuillez saisir le numéro de la case:","La caja ya está tocada, por favor, introduzca el número de la caja:",
       "La casella è già suonata, si prega di inserire il numero della casella:","The box is already played, please enter the number of the box:",
       "Dut jau grota, veskite langelio numer:","De box is al gespeeld, voer het boxnummer in:"]
err2=["Erreur, redonner le numéro de la case : ","Error, dé el número de la caja otra vez: ","Errore, ripetete il numero della scatola: ",
      "Error, re-number the box : ","Klaida, nurodykite laukelio numer:","Fout, geef het nummer van de doos:"]



# Menu partie morpion
gagne=["Félicitation vous avez gagné la partie","Felicitaciones por ganar el juego.","Congratulazioni per aver vinto la partita.",
       "Congratulations on winning the game","Sveikiname laimjus aidim","Gefeliciteerd, je hebt het spel gewonnen"]
aucun=["Pas de gagnant ! ","¡No hay ganadores! ","Nessun vincitore! ","No winner! ","Nra nugaltojo!","Geen winnaar!"]
perdu=["vous avez perdu, vous ferez mieux la prochaine fois","que perdiste, lo harás mejor la próxima vez.","Se hai perso, la prossima volta farai meglio.",
       "you lost, you'll do better next time","pralaimjote, kit kart pasiseks geriau","je hebt verloren, je zult het de volgende keer beter doen"]