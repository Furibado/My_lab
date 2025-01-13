def kolvo(stroka, per):
    return(stroka.count(per))

def dlina(stroka):
    return(len(stroka))

def kfcmod(stroka):
    if '1' in stroka:
        stroka = stroka.replace('1', 'I like chiken in KFC', stroka.count('1'))
    else:
        stroka = 'Are you dont like chiken in KFC?;('
    return(stroka)