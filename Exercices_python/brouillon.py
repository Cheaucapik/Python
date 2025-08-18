# 1️⃣ Classe Node

# Attributs : value et next

# Méthodes : rien de spécial pour le moment

# 2️⃣ Classe LinkedList

# Attribut : head (le premier nœud, None si vide)

# Méthodes à implémenter :

# __init__ : initialise la liste vide ou avec une valeur initiale.

# __repr__ : retourne la liste sous forme "LinkedList([1, 2, 3])".

# __len__ : retourne le nombre de nœuds dans la liste.

# __getitem__(self, index) : retourne la valeur du nœud à l’index donné.

# __setitem__(self, index, value) : change la valeur d’un nœud existant.

# __iter__ : permet de parcourir la liste avec une boucle for.

# __contains__ : permet d’utiliser in pour vérifier si une valeur est dans la liste.

# Bonus : @property

# Propriété first : renvoie la valeur du premier nœud.

# Propriété last : renvoie la valeur du dernier nœud.

# Propriété is_empty : renvoie True si la liste est vide.

class Node :
    def __init__(self, value, next_node = None) :
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Valeur = {self.value} et Prochain Noeud = {self.next}"

class LinkedList :
    def __init__(self, head = None) :
        if head is None :
            self.head = None
            self.size = 0
        elif isinstance(head, Node) :
            self.head = head
            self.size = 1
        else :
            raise Exception("Type invalide")

    def __repr__(self) :
        L = []
        current = self.head 
        while current is not None :
            L.append(current.value)
            current = current.next
        return f"LinkedList({L})"

    def __len__(self) :
        return self.size
    
    def __getitem__(self, index):
        if 0 <= index < self.size :
            current = self.head
            for _ in range(index) :
                current = current.next
            return current.value
        else : 
            raise IndexError("Hors des limites")
        
    def __setitem__(self, index, value):
        if 0 <= index < self.size :
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value
        else :
            raise IndexError("Hors des limites")

    def __iter__(self) :
        current = self.head
        while current is not None :
            yield current.value
            current = current.next

    def __contains__(self, value):
        current = self.head
        for _ in self.size:
            if value == current.value :
                return True
            current = current.next
        return False 

    @property
    def first(self) :
        if self.head is not None :
            return self.head.value
        return None
    
    @property
    def last(self):
        if self.head is not None :
            current = self.head
            for _ in range (self.size) :
                current = current.next
            return current.value
        return None


    @property
    def is_empty(self):
        return self.head is None

# Création des nœuds
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Affichage des nœuds
print(n1)  # Valeur = 10 et Prochain Noeud = None
print(n2)  # Valeur = 20 et Prochain Noeud = None

# Chaînage des nœuds
n1.next = n2
n2.next = n3

# Création de la linked list
L = LinkedList(n1)

# Test __repr__
print(L)  # LinkedList([10, 20, 30])

# Test __len__
print(len(L))  # 3

# Test __getitem__
print(L[0])  # 10
print(L[1])  # 20
print(L[2])  # 30

# Test __setitem__
L[1] = 25
print(L[1])  # 25
print(L)     # LinkedList([10, 25, 30])

# Test __iter__ (boucle for)
for val in L:
    print(val)  # 10, 25, 30

# Test __contains__
print(25 in L)  # True
print(20 in L)  # False

# Test propriétés @property
print(L.first)     # 10
print(L.last)      # 30
print(L.is_empty)  # False

# Test liste vide
empty_list = LinkedList()
print(empty_list)       # LinkedList([])
print(empty_list.is_empty)  # True
print(empty_list.first)     # None
print(empty_list.last)      # None

# Test IndexError
try:
    print(L[10])
except IndexError as e:
    print(e)  # Hors des limites

try:
    L[5] = 100
except IndexError as e:
    print(e)  # Hors des limites

