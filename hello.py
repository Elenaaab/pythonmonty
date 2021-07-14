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

# Python est un langage dynamique = on n'a pas besoin de lui dire le type de nos variables et fortement typé = on ne peut pas faire d'opération arithmétique sur des variables de types différents (à l'inverse de javascript qui est lui faiblement typé et convertit lui-même les variables pour faire les opérations, exemple 50 + "50" = "5050")

# =============================================================

#! TYPES SEQUENTIELS - TABLEAUX 

# =============================================================

# Simple Array

simplearray = ["elen", "bats", "monty", "python"]

# En python, un tableau indexé est appelé une "liste" et son index est appelé "indice" (qui s'utilise comme une FILE = "first in, first out" ou comme une PILE = "first in, last out")

# =============================================================

# Associative Array

mondico = {"prenom":"elen", "nom":"bats"}

# En python, un tableau associatif (avec des clés) est appelé un "dictionnaire"

mondico["prenom"]

# =============================================================

# Méthodes propres aux tableaux "listes"

# 1. Renvoyer l'index d'une valeur :
simplearray.index("elen")
# 2. Ajouter un élément à la fin de la liste :
simplearray.append("chocolat")
# 3. Ajouter un élément à une position précise : 
simplearray.insert("index", "valeur à insérer")
# 4.Supprimer le dernier élément de la liste : 
simplearray.pop()
# 5.Supprimer le premier élément qui correspond à une certaine valeur : 
simplearray.remove("valeur à supprimer")

# Méthodes propres aux tableaux "dictionnaires"

# 1. Mettre à jour 1,N valeurs (en paramètre, on insère la clé + la nouvelle valeur entre accolades) : 
mondico.update({"prenom":"tata", "nom": "yoyo"})
# 2. Pour supprimer une valeur : 
mondico.pop("nom")

# =============================================================

#Tuple

montuple = ("elen", "bats", 35)

# En python, un tuple est un tableau ordonné et non modifiable

# =============================================================

#! CONDITION SIMPLE (INDENTATION DES REPONSES : 2 espaces)

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

# =============================================================

#! BOUCLES

# =============================================================

# WHILE : tant que la condition est remplie

while user_answer != "B":
  print("essaie encore")
  user_answer = input("choisissez votre réponse")

# FOR : exécute chaque élément du tableau

for item in list:
  item.capitalize()

# =============================================================

#! MODULES

# =============================================================

# Il existe une infinité de modules natifs à Python qui exécutent différentes fonctions

# ETAPE 1 : Importer un module en ligne de commande : import random (prenons l'exemple du module RANDOM)
# ETAPE 2 : Utiliser le module : pour trouver un numéro au hasard entre deux valeurs définies : random.randint(x, y) ==> Donc nom du module.nom d'une fonction
# EXEMPLE : import turtle ==> turtle est une librairie de dessin graphique de Python (donc on peut dessiner grâce à ce module)
# EXEMPLE : import json ==> json (javascript objet notation), on crée un fichier .json et on crée une fonction qui permet de lire les éléments de ce fichier : 

def read_value_from_json(): 
   values = []
with open('fichier.json') as f:
  data = json.load(f)
  for entry in data:
    values.append(entry['mondico'])
  return values

# ==> ouvre un fichier json qui contient mes objets et charge les valeurs contenues dans mon fichier (f représente le fichier ouvert et peut être utilisé partout dans le programme)

# ATTENTION : Il faut éviter de travailler avec plusieurs modules dans le même projet.

# =============================================================

#! QUELQUES INFOS :

# =============================================================

# Côté opérateurs, nous retrouvons les classiques comparateurs(==, === et !=) et arithmétiques (+, -, *, /)
# Côté organisation, un programme Python se découpe en modules (une grande variété de modules standards existent)
# Côté utilisation, Python est un langage interprété (comme PHP), ce qui veut dire qu'il est compilé à l'exécution contrairement aux langages non interprétés (qui doivent être compilés pour être exécutés, par exemple JSX en React)
# Qu'est-ce qu'un langage de script qui différencie ces langages d'un langage de programmation pur (comme C++) ?
# Ils sont plutôt interprétés (par exemple PHP est interprété par le serveur), ils sont donc traduits en code machine par une tierce partie.