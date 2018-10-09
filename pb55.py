def miroir (k):
    K=str(k)
    r=''
    for i in range(len(K)):
        r+=str(K[len(K)-i-1])
    return int(r)


def palyndrome (n):
    if n==miroir(n):
        return 1
    else:
        return 0
    
def lychrel(n):
    i=0
    while i<=50 :
        i=i+1
        n=n+miroir(n)
        if palyndrome(n)==1:
            return False
    return True

def solution():
    s=0 #s est un compteur
    for i in range (10000):
        if lychrel(i):
            s+=1
    return(s)

assert(miroir(596)==695)
assert(palyndrome(121)==1)
assert(lychrel(349)==False)
print(solution())