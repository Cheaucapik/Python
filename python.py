# nom = "Océane"
# age = 18
# moyenne = 15.6
# estEtudiante = True

# print(f"Mon prénom est : {nom} ")
# print("Mon prenom est :", nom)
# print(f"{nom} est-elle étudiante ? {estEtudiante}")

# print(type(nom))
# print(type(age))
# print(type(moyenne))
# print(type(estEtudiante))

# moyenne = int(moyenne)
# print(moyenne)
# print(type(moyenne))

# while True :
#     age = input("Entrer votre age : ")
#     try :
#         age = int(age)
#         if age > 0 :
#             print(f"Vous avez {age} ans.")
#             break
#         else : 
#             print("Veuillez rentrer un age valide.")
#     except ValueError : 
#         print("Veuillez rentrer un age.")

# while True :
#     age = input("Entrer votre age : ")
#     if age.isdigit() :
#         age = int(age)
#         print(f"Vous avez {age} ans.")
#         break
#     else : 
#         print("Veuilez entrer un age valide.")

# import time as t

# for i in range(10, 0, -1) :
#     print(i)
#     t.sleep(1)


# dictionary_capitals = {'Madrid': 'Spain', 'Lisboa': 'Portugal', 'London': 'United Kingdom'}

# print(dictionary_capitals['Madrid'])

# dictionary_capitals["Berlin"] = "Germany"

# print(dictionary_capitals)
# print(dictionary_capitals['Berlin'])
# del dictionary_capitals['Lisboa']
# print(dictionary_capitals)
# # dictionary_capitals.clear()
# # print(dictionary_capitals)*
# print(dictionary_capitals.items())

# for ville, pays in dictionary_capitals.items() : 
#     print(f"{pays} a pour capitale {ville}")

# print(dictionary_capitals.keys())
# print(dictionary_capitals.values())

# print(type(dictionary_capitals))
# keys_list = list(dictionary_capitals.keys())
# print(keys_list[0])
# print(type(keys_list))


# list = [1, 2, 3]

# print(list)
# list.append(2)
# print(list)
# list = frozenset(list)
# print(list)
# print(type(list))