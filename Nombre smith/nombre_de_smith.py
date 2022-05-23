from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array

def som_chiff(x):
    s = 0
    n = str(x)
    for i in range(len(n)):
        s = s + int(n[i])
    return s

def premier(X):
    s = 0
    for i in range(1, X+1):
        if (X % i == 0):
            s = s + 1
    if ( s == 2 ):
        return True
    else:
        return False

def som_fact(x):
    n = x
    d = 2
    s = 0
    while (n > 1):
        if (n % d == 0):
            s += som_chiff(d)
            n = n // d
        else:
            d += 1
    return s

def Play():
    x = windows.lire_n.text()
    if (not x.isnumeric()):
        msg = "Erreur!"
    elif (som_fact(int(x)) == som_chiff(int(x))):
        msg = "c'est un nombre de smith"
    else:
        msg = "c'est pas un nombre smith"
    windows.res.setText(msg)

app = QApplication([])
windows = loadUi("inter.ui")
windows.show()
windows.verifier.clicked.connect(Play)
app.exec_()
        