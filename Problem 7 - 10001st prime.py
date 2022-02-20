#URL - https://projecteuler.net/problem=7
import math

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
      
x=3
c=0
while(c<10001):
    if(checkPrime(x)):
        c+=1
        
    x+=2
print(x)