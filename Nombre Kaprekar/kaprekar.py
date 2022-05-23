from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def partie(n, d, f):
    ch = str(n)
    return int(ch[d: f+1])

def carre(n):
    return n * n

def kaprekar(x):
    n = len(str(x))
    c = carre(x)
    p_gauche = partie(c, 0, len(str(c)) - n -1)
    p_droite = partie(c, len(str(c))-n, len(str(c)))
    somme = p_droite + p_gauche
    if (somme == x):
        return True
    else:
        return False
    

def Verifier():
    n = int(windows.lire_n.text())
    if (kaprekar(n)):
        msg = "C'est un nombre kaprekar!"
    else:
        msg ="C'est pas un nombre kaprekar!"
    windows.message.setText(msg)

app = QApplication([])
windows = loadUi("Interface.ui")
windows.show()
windows.verifier.clicked.connect(Verifier)
app.exec_()