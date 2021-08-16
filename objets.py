
#!         LES OBJETS
#! ===========================

# La POO permet de structurer son code autrement qu'en programmation procédurale. Comment écrit-on des classes en Python ? En Python, il n'y a pas besoin de prédéfinir les variables (et leur type) existant dans la classe.

# 1. CLASSE :
# ===========================

# On définit la classe via le mot CLASS, la classe prend une majuscule par convention et possède son constructeur __init__ (qui permet d'instancier des objets avec des valeurs initiales)

from abc import abstractclassmethod


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

# Instancier un objet à partir de la classe : 

newRectangle = Rectangle(6,4)
newCarre = Carre(4,4,color="blue")

# Modifier un attribut : 

newRectangle.width = 8
newCarre.color = "yellow"

# Il y a 3 types d'attributs : ceux d'instance, ceux de classe et ceux statiques.

# 1. Attribut d'instance : relatives à l'instance, elles sont accessibles avec self et définies à l'instanciation dans le constructeur
class Bird:
  def __init__(self):
    self.wings = 2

bird = Bird()
bird.wings
bird.fly()

# 2. Attribut de classe : définies directement dans le corps de la classe (accessibles via la classe sans passer par l'instanciation)

class Bird:
  names = ("mouette", "pigeon", "moineau")

Bird.names

# 3. Attribut statique : n'ont pratiquement aucun lien avec la classe (seules les méthodes peuvent être statiques) - à éviter en POO

@staticmethod

def show_bird():
  "affiche le type d'oiseau"
  return (
    "moineau"
  )

# HERITAGE de classe

# Une classe enfant copie les attributs de sa classe parent et peut réécrire les méthodes héritées (les modifier ou les surcharger):

class classeEnfant(classeParent):
  pass

# En Python, l'héritage peut être multiple mais également dangereux, il existe d'autres manières plus intéressantes pour cela : 

class classeEnfant(classeParent, autreClasseParent, EncoreUneAutreClasseParent):
  pass

# SURCHARGE de méthode

# Action de modifier les méthodes des classes parentes (il faut garder les mêmes paramètres et le même nom)

class Shape:
  def area(self):
    return 0

class Carre(Shape):
  def __init__(self, length):
    self.length = length

  def area(self):
    return length * length

# ABC "ABSTRACT BASE CLASS" : classe de base abstraite qui ne peut pas être instanciée (on doit donc créer une classe enfant pour s'en servir)

# SUPER : réutiliser le corps de la méthode parente sans devoir la réécrire (plus besoin de définir self.name) : 

class Film:
  def __init__(self, name):
      self.name = name
  def watch(self, player):
    print("bon visionnage")

class FilmCassette(Film):
  def __init__(self, name):
      super().__init__(name)
  def watch(self, player):
    if player.type != "cassette":
      print("le lecteur ne lit pas les cassettes")
    else:
      print("bon visionnage")

# Hiérarchie d'héritage : 

# Il existe de multiples niveaux d'héritage (parent, qui a un parent, qui a un parent, qui a un parent, ...)

# L'héritage est un IS A = EST UN. On hérite du parent, des grands-parents, arrières-grands parents (principe fondamental de la POO)

#A ne pas confondre avec l'héritage multiple qui veut dire qu'une classe a plusieurs parents et est à proscrire autant que possible (par exemple, cause de problème du diamant : quand deux parents ont un même modèle, duquel hérite l'enfant ?)



# 2. Objet STRING : 
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

# 3. Objet dans une COLLECTION : 
# ===========================

# Duck Typing : "si ça ressemble à un canard, alors c'est probablement un canard"
# - Les clés des dictionnaires doivent être immutables
# - Rédigez des docstrings
# - Typer votre code

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



