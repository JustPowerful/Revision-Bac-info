from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def premier(n):
    x = 0
    for i in range(1, n+1):
        if n % i == 0:
            x = x+1
    if (x == 2):
        return True
    else:
        return False
    
def Chance(ch):
    if not(ch.isnumeric() and (len(ch) == 8) and (ch[0] in ["2", "4", "5", "9"])):
        msg = "Vérifier le numéro de telephone!"
    else:
        msg = "Désolé, vous n'avez pas gagné."
        s = 0
        for i in range(len(ch)):
            s = s + int(ch[i]) * i
        if (premier(s)):
            msg = "Félicitaion, vous avez gagné."
    return msg


def Play():
    numero = windows.lire_n.text()
    message = Chance(numero)
    windows.message.setText(message)


app = QApplication([])
windows = loadUi("Interface_Jeu.ui")
windows.show()
windows.jouer.clicked.connect(Play)
app.exec_()

