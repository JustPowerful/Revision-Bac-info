from numpy import array

test = False
while test == False:
    n = int(input("Donner le nombre des cases: "))
    test = (4 <= n <= 20)
    
def trier(T, n):
    permut = True
    while (permut):
        permut = False
        for i in range(n-1):
            if (T[i] > T[i+1]):
                aux = T[i]
                T[i] = T[i+1]
                T[i+1] = aux
                permut = True
                 
def afficher(t, n):
    for i in range(n):
        print(t[i], end=" | ")

def remplir(T, n):
    for i in range(n):
        T[i] = int(input("Donner un entier n°" + str(i + 1) + ":"))

T = array([int] * n)
remplir(T, n)
trier(T, n)
afficher(T, n)

