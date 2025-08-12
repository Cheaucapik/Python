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
