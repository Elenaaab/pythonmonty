# =============================================================

# Différents types de variables cmassiques (string, int, boolean, etc) qu'on déclare sans majuscule, espace, caractère spécial

name = "elen" 
age = 35

# Python permet comme javascript, l'affectation multiple : 

name, age, gender = "elena", 35, "female"

# Pour déclarer une variable vide, j'utilise "None" avec N majuscule : 

user_answer = None

# =============================================================
# COLLECTIONS
# =============================================================

# Simple Array

simplearray = ["elen", "bats", "monty", "python"]

# En python, un tableau indexé est appelé une "liste" et son index est appelé "indice" (qui s'utilise comme une FILE = first in, first out ou comme une PILE = first in, last out)

# =============================================================

# Associative Array

mondico = {"prenom":"elen", "nom":"bats"}

# En python, un tableau associatif (avec des clés) est appelé un "dictionnaire"

mondico["prenom"]

# =============================================================

# Object

# =============================================================

#Tuple

montuple = ("elen", "bats", 35)

# En python, un tuple est un tableau ordonné et non modifiable


# =============================================================

# CONDITION SIMPLE (INDENTATION DES REPONSES : 2 espaces)

# =============================================================

if user_answer == "B":
    print("On continue le jeu")
elif user_answer =="C":
  print("l'équivalent du else if")
else:
    pass

# ELIF : c'est l'équivalent de else if en js ou elseif en PHP
# PASS : quand aucune action n'est requise : on est obligé de déclarer une réponse à Python, même si c'est pour lui dire "ne fais rien" sinon ça provoque une erreur

# =============================================================

# FONCTIONS

# =============================================================

# 1. On déclare la fonction (sans majuscule, espace, caractère spécial) et peut contenir des paramètres
# On termine la ligne par le signe : et on va à la ligne avec indentation 2 (c'est le bloc-code de notre fonction)

def hello(montableau):
  prenom = montableau[0]
  print(prenom)


# 2. On appelle la fonction pour que le programme l'exécute

hello(simplearray)

# Fonction standard (les fonctions natives de Python)

# Affiche un message dans la console (en paramètre, le message) : 
print()

# Affiche un message dans la console et attend la réponse de l'utilisateur (en paramètre, le message) :
reponse_utilisateur = input()

# Mot clé "RETURN" pour retourner la valeur de résultat ou un message : 

def hello(montableau):
  prenom = montableau[0]
  print(prenom)
  return "fonction terminée"

# =============================================================

# BOUCLES

# =============================================================

# WHILE : tant que la condition est remplie

while user_answer != "B":
  print("essaie encore")
  user_answer = input("choisissez votre réponse")

# FOR : exécute chaque élément du tableau

for item in list:
  item.capitalize()


# =============================================================

# QUELQUES INFOS :

# Côté opérateurs, nous retrouvons les classiques comparateurs(==, === et !=) et arithmétiques (+, -, *, /)
# Côté organisation, un programme Python se découpe en modules (une grande variété de modules standards existent)
# Côté utilisation, Python est un langage interprété (comme PHP), ce qui veut dire qu'il est compilé à l'exécution contrairement aux langages non interprétés (qui doivent être compilés pour être exécutés, par exemple JSX en React)
# Qu'est-ce qu'un langage de script qui différencie ces langages d'un langage de programmation pur (comme C++) ?
# Ils sont plutôt interprétés (par exemple PHP est interprété par le serveur), ils sont donc traduits en code machine par une tierce partie.