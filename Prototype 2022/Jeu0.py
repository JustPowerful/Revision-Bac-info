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