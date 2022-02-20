#URL - https://projecteuler.net/problem=10

import math
l=2000000
def checkPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    f=int(math.sqrt(n))+1
    while(i<f):
        if(n%i==0):
            return False
        i+=1
    return True
s=0
for x in range(2,l+1):
    if(checkPrime(x)):
        s+=x
    print(x)
print(s)