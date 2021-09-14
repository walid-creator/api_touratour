########## Fonction de hashage ###########
# permet de hasher le mot de passe

import hashlib

def hash_mdp(mdp, pseudo):
    salt = pseudo
    return hashlib.sha224(mdp.encode()+salt.encode()).hexdigest()
