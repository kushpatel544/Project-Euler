#URL - https://projecteuler.net/problem=3

n = 600851475143

def checkPrime(p):
    c=0
    x=p
    while(x>0 and c<3):
        if(p%x==0):
            c+=1
        x-=1
    if(c==2):
        return True
    else:
        return False
p=2

while(n!=1):
    while(checkPrime(p) and n%p==0):
        n=n/p
        print(n,p)
    p+=1




