import numpy as np

#Les array

l = [1,2,3]

array = np.array([[0, 1, 2, 3], 
                  [4, 5, 6, 7], 
                  [8, 9, 10, 11],
                  [12, 13, 14, 15]])

print(array[2:,0:2])

print(np.ndim(array)) #Donne la dimension de l'array
print(np.shape(array)) #Donne la taille de l'array (lignes, colonnes)


array = np.array([9.1234, 81.122, 25.5555])
array2 = np.array([1, 2, 3])

#méthodes array

print(array - 1)
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.round(np.sqrt(array)))
print(np.pi)
print(array / array2)

scores = np.array([1, 15, 16, 20, 12, 9])
print(scores == 20)
print(scores >=10)
scores[scores < 10] = 0
resultat = scores.astype(str)
resultat[resultat != '0'] = "passe"
resultat[resultat == '0'] = "ne passe pas"
print(resultat)

scores = np.array([1, 15, 16, 20, 12, 9])
scores = np.where(scores < 10, 0, scores)
resultat = np.where(scores == 0, "ne passe pas", "passe")
print(resultat) 

nombre = 42 
txt = str(nombre)
print(txt)
print(type(txt))

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

array2 = np.array([[1, 2, 3],
                 [5, 6, 7],
                 [9, 10, 11],
                 [12, 13, 14]])

print(np.dot(array2, array))
print(np.shape(array))
print(np.shape(array2))

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

array2 = np.array([[1, 2, 3, 4]])

print(array*array2)

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])

print(np.sum(array, axis = 0))
print(np.sum(array, axis = 1))

rng = np.random.default_rng(seed=1)
print(rng.integers(1, 101, size=(3,2)))
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

#float
import numpy as np
pi = np.pi
print(f"{pi = :.2f}")

#mask

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mask = np.where(arr%2 == 0)
print(arr[mask])

#funky indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr[[1, 4]] = [999, 999]
print(arr)

#reshape and clip
arr = np.arange(1, 13).reshape(3, 4)  
arr[1, 3] = 999
print(arr)

arr2 = np.arange(13, 25).reshape(3, 4)  
print(arr2)
arr2 = np.clip(arr2, 13, 20)
print(arr2)