def TRI_LISTE(file):
    L=file.split(',')
    L.sort()
    return L

def SCORE(mot):
    s=0
    for i in range (1, len(mot)-1):
        s+=ord(mot[i])-64
    return s

def solution (file):
    total=0
    noms=TRI_LISTE(file.read())
    for i in range (len(noms)) :
        total+=SCORE(noms[i])*(i+1)
    return total


assert(SCORE('"COLIN"')==53)
fichier=open('names.txt','r')
print(TRI_LISTE(fichier))
print(solution(fichier))