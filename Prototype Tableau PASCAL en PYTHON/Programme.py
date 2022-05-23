from numpy import array

def somevoy(ch):
    n = 0
    for i in range(len(ch)):
        if (ch[i] in ["O", "I", "Y", "E", "A", "U"]):
            n = n + 1
    return n

def formerTi(t, ti, n):
    for i in range(n):
        nom = t[i]
        ch_a = nom[0: 2]
        ch_b = str(i+1)
        somme = ord(nom[0]) + somevoy(nom)
        if somme > 90:
            ch_c = "a"
        else:
            ch_c = chr(somme)
        ti[i] = ch_a + ch_b + ch_c
        

def afficher(t, n):
    for i in range(n):
        print(t[i], end=" | ")

def remplir(T, n):
    for i in range(n):
        testa = False
        while (testa == False):
            T[i] = input("Donner le nom d'utilisateur n°" + str(i + 1) +":")
            j = -1
            nom = T[i]
            testb = False
            while (testb == False):
                j = j + 1
                testb = not("A" <= nom[j] <= "Z") or (j == len(nom) - 1)
            testa = ("A" <= nom[j] <= "Z") and (len(nom) <= 20)
 
 
test = False
while (test == False):
    n = int(input("Donner le nombre d'utilisateurs: "))
    test = (1 <= n <= 9)

T = array([str] * n)
Ti = array([str] * n)
remplir(T, n)
formerTi(T, Ti, n)
afficher(Ti, n)
