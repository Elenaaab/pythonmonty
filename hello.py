# =============================================================

#! VARIABLES & TYPES NATIFS

# =============================================================

# Différents types natifs (string, int, boolean, etc) qu'on déclare sans majuscule, espace, caractère spécial
name = "elen" 
age = 35

# Python permet comme javascript, l'affectation parallèle : 
name, age, gender = "elen", 35, 'female'

# Et l'affectation multiple : 
a=b=c=5

# Pour déclarer une variable vide, j'utilise "None" avec N majuscule : 
user_answer = None

# En Python, tous les objets peuvent être vrais (truthy) ou faux (falsy). Tous les types natifs de base ont des valeurs true/false prédéfinies.

# "Garbage collector" : Python se charge pour nous de la gestion de la mémoire. Python ne crée pas un nouvel objet en mémoire, il pointe les deux variables vers la même valeur (l'objet int 5). Si on réassigne des valeurs aux deux variables, Python comprend que l'objet 5 n'est plus associé à une variable et il se charge de le supprimer de la mémoire du script.
nombre = 5
nombre_2 = nombre

#  La fonction id(mavariable) retourne la place en mémoire de l'objet déclaré par mavariable
id(nombre_2)

# Python applique des processus d'optimisation :

# SINGLETON = objet unique
id(True)
id(True)
# TRUE possède un ID unique dans le script

# De -5 à 256 les nombres auront automatiquement le même ID dans le script
id(5)
id(5)
# = même ID retourné par le script
id(500)
id(500) 
# = ID différents retournés
a=5
id(a)
# = même ID retourné par le script que si on faisait id(5)

# Concaténer deux valeurs : il faut transformer les types pour qu'ils soient égaux
a= "j'ai " + str(10) + "euros"
b= str(10) + str(5) != str(10+5)

# Python est un langage dynamique = on n'a pas besoin de lui dire le type de nos variables et fortement typé = on ne peut pas faire d'opération arithmétique sur des variables de types différents (à l'inverse de javascript qui est lui faiblement typé et convertit lui-même les variables pour faire les opérations, exemple 50 + "50" = "5050")

# =============================================================

#! TYPES SEQUENTIELS - TABLEAUX 

# =============================================================

# Simple Array

liste = []
simplearray = ["elen", "bats", "monty", "python"]

# En python, un tableau indexé est appelé une "liste" et son index est appelé "indice" (qui s'utilise comme une FILE = "first in, first out" ou comme une PILE = "first in, last out")
#La liste est un objet mutable

# =============================================================

# Associative Array

mondico = {"prenom":"elen", "nom":"bats"}

# En python, un tableau associatif (avec des clés) est appelé un "dictionnaire"

mondico["prenom"]

# =============================================================

# Méthodes propres aux tableaux "listes"

# 1. Renvoyer l'index d'une valeur :
simplearray.index("elen")
# 2. Ajouter un/plusieurs élément(s) à la fin de la liste :
simplearray.append("chocolat")
simplearray.extend([10, 5, 18])
# 3. Ajouter un élément à une position précise : 
simplearray.insert("index", "valeur à insérer")
# 4.Supprimer un élément précis de la liste selon son index : 
simplearray.pop("2")
# 5.Supprimer le premier élément qui correspond à une certaine valeur : 
simplearray.remove("valeur à supprimer")
# 5B. Supprimer tous les éléments : 
simplearray.clear()
# 6 Chercher un élément dans une liste - les "slice" :

simplearray[0:5]
#- On pointe une tranche de la liste : on récupère les 5 premiers éléments de la liste
print(simplearray[:])
#- Pour récupérer tous les éléments
print(simplearray[:-1])
#- Pour récupérer tous les éléments sauf le dernier
print(simplearray[2:])
#- Pour récupérer les éléments à partir de l'élément 2
print(simplearray[::2])
#- Pour récupérer un élément sur 2
print(simplearray[1:-2:2])
#- Pour récupérer les éléments un élément sur 2, jusqu'au 4e element donc on récupère 2 et 4
print(simplearray[::-1])
#- Pour récupérer les éléments dans l'ordre inversé

#7. Récupérer l'index d'un élément : 
indexitem = simplearray.index("chocolat")
#8. Compter les occurences de la liste :
choco = simplearray.count("chocolat")
#9. Trier la liste (la méthode trie mais revoie "none") : 
simplearray.sort()
#10. Trier la liste et renvoie la liste triée qui se fait enregistrer dans la variable "choco"
choco = sorted(simplearray)
#11. Inverser les éléments : 
simplearray.reverse()

#12. JOIN : Ajouter des éléments dans une liste pour l'affichage par exemple : 
resultat = " ".join(simplearray)
# On ajoute un espace vide entre chaque élément

resultat = "\t".join(simplearray)
# On affiche chaque élément à la ligne

# Méthodes propres aux tableaux "dictionnaires"

# 1. Mettre à jour 1,N valeurs (en paramètre, on insère la clé + la nouvelle valeur entre accolades) : 
mondico.update({"prenom":"tata", "nom": "yoyo"})


# =============================================================

#Tuple

montuple = ("elen", "bats", 35)

# En python, un tuple est un tableau ordonné et non modifiable (immutable)

# =============================================================

#! STRUCTURES CONDITIONNELLES (INDENTATION DES REPONSES : 2 espaces)

# =============================================================

# On termine la ligne par le signe : et on va à la ligne avec indentation 2 (c'est le bloc-code de notre fonction) 

if user_answer == "B":
    print("On continue le jeu")
elif user_answer =="C":
  print("l'équivalent du else if")
else:
    pass

# ELIF : c'est l'équivalent de else if en js ou elseif en PHP
# PASS : quand aucune action n'est requise : on est obligé de déclarer une réponse à Python, même si c'est pour lui dire "ne fais rien" sinon ça provoque une erreur

# Opérateur ternaire : 

age = 20
majeur = True if age>= 18 else False

# Opérateurs logiques AND - OR - NOT (pour associer plusieurs conditions ensemble) : 

if name == "elen" and age>= 35:
    print("true and true donc ok")

if name == "elen" or age>= 20:
    print("un est true donc ok")

# AND est prioritaire sur OR sauf si on spécifie les priorités : 

if 5 > 2 and (5 < 10 or 5 > 15):
    print("true and au moins un true donc ok")

if not name == "elen":
    print("on se connait ?")

# =============================================================

#! FONCTIONS

# =============================================================


# Comment ça marche ? 

# 1. On déclare la fonction (sans majuscule, espace, caractère spécial) et peut contenir des paramètres
# On termine la ligne par le signe : et on va à la ligne avec indentation 2 (c'est le bloc-code de notre fonction)
def hello(montableau):
  prenom = montableau[0]
  print(prenom)


# 2. On appelle la fonction pour que le programme l'exécute
hello(simplearray)


# EXEMPLES : 


# 0. Affiche un message dans la console (en paramètre, le message) : 
print()

# Affiche un message dans la console et attend la réponse de l'utilisateur (en paramètre, le message) :
reponse_utilisateur = input()

# Mot clé "RETURN" pour retourner la valeur de résultat ou un message : 

def hello(montableau):
  prenom = montableau[0]
  print(prenom)
  return "fonction terminée"

# 1. Transformer une chaine de caractères en liste :
hello = "hello world"
hello.split()
# ===>résultat :
['hello', 'world'] 

# 2. Enlever les espaces vides autour d'une chaine de caractères:
hey = "     hey     "
hey.strip()
# ===>résultat :
'hey'

# 3. Mettre tous les caractères en MAJ ou en MIN : 
hello.upper()
hello.lower()

# 4. Remplacer des valeurs à l'intérieur d'une chaine (valeurs des variables en paramètres) : 
"{personnage} a dit: {citation}".format(personnage="tata",citation="yoyo")
# Ca fonctionnerait sans nommer les variables, grâce à l'ordre des valeurs
"{} a dit: {}".format("tata","yoyo")

# 5. Vérifier qu'un nombre est en entier ou pas (retourne un booléen): 
(2.5).is_integer()

# 6. Convertir une chaine de caractère en nombre : 
a=5
b="10"
b=int(b)
print(a+b)

# 7. Convertir un nombre en chaine de caractères : 
a = str(10)

# 8. Demander une valeur à l'utilisateur : 
input("entrez un nombre :")

# ==> Récupérer l'info 
variable = input("entrez un nombre :")
# ==> Afficher l'info
print(variable)

# =============================================================

#! BOUCLES

# =============================================================

# WHILE : tant que la condition est remplie (danger : aboutir sur une boucle infinie, si on ne donne pas une condition de sortie)

while user_answer != "B":
  print("essaie encore")
  user_answer = input("choisissez votre réponse")

i = 0

while i < 10000:
  print("bonjour")
  i += 1

import time

while True:
  print("sauvegarde en cours")
  time.sleep(600)

# FOR : exécute chaque élément du tableau

for item in list:
  item.capitalize()

# 1. Instructions CONTINUE et BREAK pour sortir d'une boucle

newListe = ["1", "4", "Paul", "3", "Pierre"]

for element in newListe:
  if element.isdigit():
    continue
  print(element)
  # Va donc afficher Paul et Pierre

for element in newListe:
  if element.isdigit():
    break
  print(element)
  # N'affichera rien car sortira de la boucle avant d'arriver à Paul

# 2. Les compréhensions de listes (itérer sur des listes grâce à des structures conditionnelles, sur une même ligne)

exempleList = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

nombres_positifs = []
for i in exempleList:
  if i > 0:
    nombres_positifs.append(i)
    
# =============================================================

#! MODULES (voir fiche)

# =============================================================

# Il existe une infinité de modules natifs à Python qui exécutent différentes fonctions

# ETAPE 1 : Importer un module en début de fichier : import random (exemple du module RANDOM)
# ETAPE 2 : Utiliser le module : pour trouver un numéro au hasard entre deux valeurs définies : random.randint(x, y) ==> Donc nom du module.nom d'une fonction
# EXEMPLE : import turtle ==> turtle est une librairie de dessin graphique de Python (donc on peut dessiner grâce à ce module)
# EXEMPLE : import json ==> json (javascript objet notation), on crée un fichier .json et on crée une fonction qui permet de lire les éléments de ce fichier : 

# =============================================================

#! TYPES D'ERREUR :

# =============================================================

#1. Erreur de syntaxe : oubli de ponctuation, d'indentation, casse, utilisations de mots réservés. L'interpréteur montre où il s'est arrêté dans le code avec un ^ et donne des indications sur l'erreur.
#2. Erreur à l'exécution : variables non définies, méthodes appliquées à variables de mauvais types. Python indique de quel type est l'erreur
#3. Erreur sémantique : dites "erreurs de logique" quand le script ne renvoie pas à ce qu'on avait planifié.Il existe des débuggeurs qui exécutent le script pas à pas afin qu'on suive le chemin de l'ordinateur.

# =============================================================

#! QUELQUES INFOS :

# =============================================================

# Côté opérateurs, nous retrouvons les classiques comparateurs(==, === et !=) et arithmétiques (+, -, *, /)
# Côté organisation, un programme Python se découpe en modules (une grande variété de modules standards existent)
# Côté utilisation, Python est un langage interprété (comme PHP), ce qui veut dire qu'il est compilé à l'exécution contrairement aux langages non interprétés (qui doivent être compilés pour être exécutés, par exemple JSX en React)
# Qu'est-ce qu'un langage de script qui différencie ces langages d'un langage de programmation pur (comme C++) ?
# Ils sont plutôt interprétés (par exemple PHP est interprété par le serveur), ils sont donc traduits en code machine par une tierce partie.