#URL - https://projecteuler.net/problem=3

import math
n = 600851475143

def checkPrime(p):
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    i = 3
    f=int(math.sqrt(p))+1
    while(i<f):
        if(p%i==0):
            return False
        i+=1
    return True
p=2

while(n!=1):
    while(checkPrime(p) and n%p==0):
        n=n/p
        print(n,p)
    p+=1




