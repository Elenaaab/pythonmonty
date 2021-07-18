import random
import os

# =============================================================

#! MODULES

# =============================================================

#TODO Module RANDOM : 

r = random.randint(0.1)
r = random.uniform(0, 1)
#affichent des nombres au hasard, randint un entier, uniform un float

r = random.randrange(0,101,10)
#affiche des nombres au hasard entre 0 et 101 avec une intervale de 10

#TODO Module OS (qui permet de créer des dossiers) : 

#1. import os
#2. on déclare le chemin du dossier dans une variable
chemin = "/Users/trinity/html/saison1/episode1"

#3. On utilise la fonction join pour concaténer le nom du dossier à créer et le chemin (on peut ajouter en dernier paramètre avec les sous dossiers éventuels exemple ,"sous-dossier")
dossier = os.path.join(chemin, "dossier")

#4. On utilise la fonction makedir pour créer le dossier
if not os.path.exists(dossier): 
    os.makedirs(dossier)

#5. On peut supprimer le dossier (avec la fonction makedirs et removedirs, si le dossier existe déjà, ou est déjà supprimé, ça fait une erreur)
if os.path.exists(dossier): 
    os.removedirs(dossier)

#TODO ===> Quelque soit le module, on peut afficher toutes les fonctions qu'il contient grâce à print(dir(module))
print(dir(os))

#TODO ===> Permet d'afficher la "docustring" donc documentation sur les fonctions : help(module.fonction) (on quitte l'aide via touche Q)
help(os.removedirs)

#TODO ===> Permet d'afficher de manière plus lisible les fonctions du module via le module pprint (le module pprint ne peut pas être appelé mais sa fonction oui) : 
from pprint import pprint
print (dir(random))

# Les fonctions avec des ___ sont dites "privées" c'est Python qui les utilise, pas nous.

# =============================================================

# Les objets CALLABLES (appelables) : 

# =============================================================

# On peut vérifier ce qui est appelable via la fonction : print(module.fonction()) ou pprint(callable(module.fonction()))

