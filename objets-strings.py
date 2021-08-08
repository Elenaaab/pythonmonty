
#!         LES OBJETS
#! ===========================

# La POO permet de structurer son code autrement qu'en programmation procédurale. Comment écrit-on des classes en Python ? En Python, il n'y a pas besoin de prédéfinir les variables (et leur type) existant dans la classe.

# On définit la classe via le mot CLASS, la classe prend une majuscule par convention et possède son constructeur __init__ (qui permet d'instancier des objets avec des valeurs initiales)

class Rectangle:
  width = 3
  height = 2
  def calcul_area(self):
    return self.width * self.height

class Carre:
  def __init__(self, lenght, width, color="red"):
    self.length = lenght
    self.width = width
    self.color = color

# 1. Les objets STRING : 
# ===========================

# Il existe des centaines de méthodes en Python, l'important est de s'en savoir et de penser à aller chercher dans la doc, la méthode appropriée à ce qu'on cherche à faire dans un script

#1. Changer la casse (upper, lower, capitalize, title - lettre maj à chaque mot) : 
"Bonjour".upper()

#2. Remplacer/modifier des éléments : 
"Bonjour".replace("jour", "soir")

#3. Supprimer des éléments (strip agit en partant du début et de la fin de la string jusqu'à rencontrer l'élément à retirer et par défaut, donc sans paramètre retire les espaces) :
" bonjour ".strip()
" bonjour ".strip(" ujor")
= 'bon'

# Strip peut prendre une restriction "depuis la gauche" = lstrip() ou "depuis la droite" = rstrip()
" bonjour ".rstrip(" ujor")
= ' bon'

#4. Séparer SPLIT et joindre JOIN des éléments qu'on peut utiliser ensemble pour reconstituer différemment les valeurs : 
"1, 2, 3, 4, 5".split(", ")
= '1', '2', '3', '4', '5'

"-".join("1, 2, 3, 4, 5".split(", "))
= "1-2-3-4-5"

#5. Remplir de zéro (utile si on fait des séquences par exemple) : 
"9".zfill(4)
= "0009"

#6. Les méthodes "is" pour vérifier ce que contient une string retournent un booléen : 
"bonjour".islower()
"bonjour".istitle()

"bonjour".isdigit()
#false (car pas numérique)
"50".isdigit()
#true (car numérique)
"50a".isdigit()
#false (car le caractère l'emporte)

#7. Compter le nombre d'occurences : 
"bonjour le jour".count("jour")
#retourne 2
"bonjour le jour".count(" jour")
#retourne 1

#8. Trouver une suite de caractères : 
"bonjour le jour".find("jour")
"bonjour le jour".index("jour")
#les 2 retourne 3 car ils trouvent la suite au 4e caractère de la chaine (la différence est que find retournera -1 s'il ne trouve pas la suite, index retournera une erreur)
"bonjour le jour".rfind("jour")
#retourne 11 car il part de la fin

#9. Vérifier une suite de caractères
"image.png".endswith("png")
#true
"image.png".startswith("image")
#true

# ===========================
# LES OPERATEURS
# ===========================

# Les mathématiques : +, -, /, * (attention la division retourne un nombre décimal, un float)

# MODULO % permet de récupérer le reste d'une division
6 % 4 = 2

# DIVISION ENTIERE // permet de récupérer une division sans décimal 
10 // 3 = 3

# PUISSANCE **
2**4 = 16

#  =, +=, -=, /=, *=, //=, **=, %= (assignation), == (comparaison : égal), != (différent), <=, >=, >, < (plus petit, grand)

# IS (différent de ==) : == permet de vérifier l'égalité des valeurs, tandis que IS permet de vérifier si deux objets sont les mêmes en mémoire
a = [1, 2, 3]
b = [1, 2, 3]
a == b
#true
a is b
#false

# ===========================
# FORMATAGE
# ===========================

# f-string (pour indiquer où on veut entrer la variable on met f en début de phrase), on peut même y faire des opérations : 
prenom = "Paul"
f"Bonjour {prenom} ! "

a = 5
b = 2
f"j'ai {a * b} euros dans mon sac"
#retourne "j'ai 10 euros dans mon sac"

# méthode format (avec et sans indice - l'indice perme de mettre plusieurs valeurs et/ou de les répéter):
age = 26
phrase = "J'ai {} ans".format(age)
phrase = "J'ai {tatayoyo} ans".format(tatayoyo = age)

#f-string est beaucoup plus utilisé mais requiert que la variable soit disponible, donc déjà définie, alors que la méthode format n'exige pas que la variable existe déjà, elle ne retourne pas d'erreur



