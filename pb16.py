M=2**1000
def pb16 (n):
    c=str(n) #creation d'une chaine de caractère à partir de n
    S=0 #S=compteur
    for i in range (0,len(c)):
        S=S+int(c[i]) #somme des digits
    return S

assert pb16(11)==2

print(pb16(M))

