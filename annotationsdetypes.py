#  =========================

#! LES ANNOTATIONS DE TYPE (TYPE HINTING) :  

#  =========================

#   Python est un langage fortement typé et interprété, les annotations de type sont un moyen d'éviter les erreurs via les vérifications et de bien documenter le code :

# Dans la définition de la fonction, il suffit de mettre le type du paramètre avec : et la valeur de retour grâce à ->
def add(a:int, b:float) -> float:
  return a + b

# On peut aussi ajouter les valeurs par défaut APRES le type hinting : 
def add(a:int = 0, b: float = 1.2):
  return a + b

# Types complexes, une liste : 
def add(a: list[int]) -> list[int]:
  return [1, 2, 3]

# Types simples hors fonction, les variables : 
a: int = "5"

# Ce n'est pas obligatoire et pas systématique, on peut en mettre là où on trouve ça utile.

# Sur VSCode, l'extension Pylance permet de détecter les annotations de type (elle est installée automatiquement avec Python)