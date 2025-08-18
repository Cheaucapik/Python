#type et format

nom = "Océane"
age = 18
moyenne = 15.6
estEtudiante = True

print(f"Mon prénom est : {nom} ")
print("Mon prenom est :", nom)
print(f"{nom} est-elle étudiante ? {estEtudiante}")

print(type(nom))
print(type(age))
print(type(moyenne))
print(type(estEtudiante))

moyenne = int(moyenne)
print(moyenne)
print(type(moyenne))


#round sans round
moyenne2 = 15.123456789
print(f"{moyenne2:.2f}")

#Deux algorithmes sur l'âge

while True :
    age = input("Entrer votre age : ")
    try :
        age = int(age)
        if age > 0 :
            print(f"Vous avez {age} ans.")
            break
        else : 
            print("Veuillez rentrer un age valide.")
    except ValueError : 
        print("Veuillez rentrer un age.")

while True :
    age = input("Entrer votre age : ")
    if age.isdigit() :
        age = int(age)
        print(f"Vous avez {age} ans.")
        break
    else : 
        print("Veuilez entrer un age valide.")

#Faire un countdown 

import time as t

for i in range(10, 0, -1) :
    print(i)
    t.sleep(1)


#Les dictionnaires python 

dictionary_capitals = {'Madrid': 'Spain', 'Lisboa': 'Portugal', 'London': 'United Kingdom'}

print(dictionary_capitals['Madrid'])

dictionary_capitals["Berlin"] = "Germany"

print(dictionary_capitals)
print(dictionary_capitals['Berlin'])
del dictionary_capitals['Lisboa']
print(dictionary_capitals)
# dictionary_capitals.clear()
# print(dictionary_capitals)
print(dictionary_capitals.items())

for ville, pays in dictionary_capitals.items() : 
    print(f"{pays} a pour capitale {ville}")

print(dictionary_capitals.keys())
print(dictionary_capitals.values())

print(type(dictionary_capitals))
keys_list = list(dictionary_capitals.keys())
print(keys_list[0])
print(type(keys_list))

#fronzenset 

list = [1, 2, 3]

print(list)
list.append(2)
print(list)
list = frozenset(list)
print(list)
print(type(list))

#Exercices de compréhensions des boucles

set_comp = {i%3 for i in range(10)}

set_comp= {}
for i in range(10):
    set_comp.add(i%3)

gen_comp = (2*x+5 for x in range(10))

def gen() : 
    for x in range(10):
        yield 2*x+5
gen_comp = gen()

for i in gen_comp:
    print(i)

print(next(gen_comp))


#Niveau 1 

#1. 

carre = [n**2 for n in range(1, 10)]

#2.

cubes = [n**3 for n in range(5)]

cubes = []
for n in range(5) :
    cubes.append(n**3)

#Niveau 2

#3.

pairs = [i for i in range(1, 20) if i%2 == 0]

#4 

small_odds = [n for n in range(1, 10) if n % 2 == 1]

small_odds = []

for n in range(1, 10) :
    if n%2 ==1 :
        small_odds.append(n)

#Niveau 3

#5 
dict_carre = {n : n**2 for n in range (5)}

#6
fruits = ['pomme', 'banane', 'poire', 'pomme']
set_comp = {len(n) for n in fruits}

#Niveau 4

#7

gen = (2*n+1 for n in range(6))

for val in gen :
    print(val)

#8

gen = (n**2 for n in range(4))

def gen():
    for n in range(4):
        yield n**2


#Python Tutorial: Comprehensions - How they work and why you should be using them

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
my_list = [n for n in nums]

#2
my_list = [n*n for n in nums]

#3
my_list = [n for n in nums if n%2 == 0]

#4
my_list = [(l,n) for l in 'abcd' for n in range(4)]
print(my_list)

#5
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {names[i]:heros[i] for i in range(len(names))}
print(my_dict)

my_dict = {name:hero for name, hero in zip(names, heros)}
print(my_dict)

#If name not equal to Peter
my_dict = {name:hero for name, hero in zip(names, heros) if name !="Peter"}
print(my_dict)

#6
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = {n for n in nums}

#7
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_gen = (n*n for n in nums)
for n in my_gen :
    print(n)


#Exercice sur des if, or, et string venant de BroCode : python Course 2024

while True : 
    username = input("Entrer votre nom : ")
    if(len(username) <= 12 and username.find(" ") and username.find(" ") < 0 and username.isalpha()) :
        print("Username granted")
        break
    else : 
        print("No es possible")

#réinitialiser une variable :
def reset(var) :
    return type(var)()

l = [1, 2, 3]
print(l)
print(id(l))
l = reset(l)
print(l)
print(id(l))

a = 10
print(hex(a))

import time

#Objectif : Créer un décorateur qui mesure le temps d’exécution d’une fonction et affiche combien de fois la fonction a été appelée.

def tps_exec(f) :
    f.calls = 0
    def wrap(*args) :
        t1 = time.time()
        result = f(*args)
        f.calls += 1
        t2 = time.time()
        print(t2 - t1)
        return result, f.calls
    return wrap

@tps_exec
def sum_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_numbers(3))
print(sum_numbers(4))

# Objectif : Créer un décorateur qui vérifie les arguments passés à une fonction avant de l’exécuter.

def validate_args(f) :
    def warp(*args, **kwargs) :
        if args[0] >= 0 :
            result = f(*args, **kwargs)
            return result
        else :
            raise ValueError("Sorry no numbers below 0.")
    return warp

@validate_args
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial(1))
print(factorial(-152))

# Crée une classe BankAccount qui :

# Possède un attribut privé _balance (le solde).

# Utilise un getter balance pour pouvoir lire le solde.

# Utilise un setter balance pour mettre à jour le solde, mais seulement si le nouveau solde est positif.

# Si on essaie de mettre un solde négatif, le setter doit afficher un message d’erreur et ne rien changer.

class BankAccount :
    def __init__(self, balance) :
        self._balance = balance


    @property
    def balance(self) :
        return self._balance
    
    @balance.setter
    def balance(self, new_balance) :
        if new_balance > 0 :
            self._balance = new_balance
        else : 
            raise ValueError("Entrer une valeur positive")

account = BankAccount(100)
print(account.balance)   # 100

account.balance = 200
print(account.balance)   # 200

account.balance = -50    # ❌ Affiche une erreur, ne change pas le solde
print(account.balance)   # 200

#Dunder methods

# Objectif

# Créer une classe Fraction qui représente une fraction a/b et qui supporte :

# L’affichage lisible (__str__)

# Une représentation officielle (__repr__)

# L’addition (__add__)

# La multiplication (__mul__)

# La comparaison (__eq__)

# Réduire automatiquement les fractions (2/4 → 1/2)

# Ajouter __sub__ et __truediv__

from math import gcd

class Fraction :
    def __init__(self, num, denom) :
        if denom == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être 0")
        
        div = gcd(num, denom)
        num = num//div
        denom = denom//div
        if denom < 0 :
            num, denom = -num, -denom
        self.num = num
        self.denom = denom

    def __str__(self) :
        return f"{self.num}/{self.denom}"
    
    def __repr__(self):
        return f"numérateur = '{self.num}', dénominateur = '{self.denom}'"
    
    def __add__(self, other) :
        if isinstance(other, Fraction) :
            num = self.num * other.denom + self.denom * other.num
            denom = self.denom * other.denom
            return Fraction(num, denom)
        elif isinstance(other, int) :
            denom = other * self.denom
            num = self.num * other + self.denom * denom
            return Fraction(num, denom)
        raise Exception("Type invalide")

    def __mul__(self, other) :
        if isinstance(other, Fraction) :
            return Fraction(self.num * other.num, self.denom * other.denom)
        elif isinstance(other, int) :
            return Fraction(self.num * other, self.denom)
        raise Exception("Type invalide")

    def __eq__(self, other):
        if isinstance(other, Fraction) :
            return self.num == other.num and self.denom == other.denom
        return False
    
    def __sub__(self, other): 
        if isinstance(other, Fraction) :
            num = self.num * other.denom - self.denom * other.num
            denom = self.denom * other.denom
            return Fraction(num, denom)
        elif isinstance(other, int) :
            denom = other * self.denom
            num = self.num * other - self.denom * denom
            return Fraction(num, denom)
        raise Exception("Type invalide")

    def __truediv__(self, other) :
        if isinstance(other, Fraction) :
            num = self.num * other.denom
            denom = self.denom * other.num
            return Fraction(num, denom)
        elif isinstance(other, int) :
            return Fraction(self.num, self.denom * other)
        raise Exception("Type invalide")
    
# =====================
# TESTS DE LA CLASSE FRACTION
# =====================

f1 = Fraction(2, 4)    # doit se réduire en 1/2
f2 = Fraction(3, 9)    # doit se réduire en 1/3
f3 = Fraction(-2, -4)  # doit devenir 1/2
f4 = Fraction(4, -6)   # doit devenir -2/3

print("=== Affichage ===")
print("f1 =", f1)      # 1/2
print("f2 =", f2)      # 1/3
print("f3 =", f3)      # 1/2
print("f4 =", f4)      # -2/3
print("repr(f1) =", repr(f1))  # Fraction(1, 2)

print("\n=== Addition ===")
print("f1 + f2 =", f1 + f2)  # 1/2 + 1/3 = 5/6
print("f1 + 1 =", f1 + 1)    # 1/2 + 1 = 3/2

print("\n=== Soustraction ===")
print("f1 - f2 =", f1 - f2)  # 1/2 - 1/3 = 1/6
print("f1 - 1 =", f1 - 1)    # 1/2 - 1 = -1/2

print("\n=== Multiplication ===")
print("f1 * f2 =", f1 * f2)  # 1/2 * 1/3 = 1/6
print("f1 * 3 =", f1 * 3)    # 1/2 * 3 = 3/2

print("\n=== Division ===")
print("f1 / f2 =", f1 / f2)  # (1/2) / (1/3) = 3/2
print("f1 / 2 =", f1 / 2)    # (1/2) / 2 = 1/4

print("\n=== Comparaison ===")
print("f1 == f3 ?", f1 == f3)   # True (1/2 == 1/2)
print("f1 == f2 ?", f1 == f2)   # False (1/2 != 1/3)
print("f1 == Fraction(4, 8) ?", f1 == Fraction(4, 8))  # True (1/2 == 1/2)

import math as math

class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y 

    def __repr__(self) :
        return f"Vecteur : Point x = {self.x}, Point y = {self.y}"

    def __add__(self, other) :
        if isinstance(other, Vector2D) :
            return Vector2D(self.x + other.x, self.y + other.y)
        raise Exception("Type invalide")
    
    def __sub__(self, other) :
        if isinstance(other, Vector2D) :
            return Vector2D(self.x - other.x, self.y - other.y)
        raise Exception("Type invalide")

    def __mul__(self, other) :
        if isinstance(other, Vector2D) :
            return Vector2D(self.x * other.x, self.y * other.y)
        raise Exception("Type invalide")
    
    def __abs__(self) :
        return math.sqrt(self.x**2 + self.y**2)
    
    def __len__(self) : 
        return 2
    
    def __eq__(self, other) :
        if isinstance(other, Vector2D) : 
            return self.x == other.x and self.y == other.y
        
    def __getitem__(self, index) :
        if index == 0 :
            return self.x
        elif index == 1 :
            return self.y
        raise IndexError("Hors des limites") 

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print(v1)          # (1, 2)
print(repr(v2))    # Vector2D(x=3, y=4)

print(v1 + v2)     # (4, 6)
print(v1 - v2)     # (-2, -2)
print(v1 * v2)     # 11 (produit scalaire)

print(abs(v1))     # √(1² + 2²) = 2.236...
print(len(v1))     # 2

print(v1 == Vector2D(1, 2))   # True
print(v1 == v2)               # False

print(v1[0])
print(v1[1])
