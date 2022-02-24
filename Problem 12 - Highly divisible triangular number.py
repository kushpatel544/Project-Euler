#URL - https://projecteuler.net/problem=12

import math
n, i, c = 0, 1, 0

# Using Brute Force
# def Cdiv(n):
#     k=0
#     for x in range(1,n+1):
#         if(n%x==0):
#             k+=1
#     return k

#Using prime factorization
def checkPrime(p):
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    a = 3
    f=int(math.sqrt(p))+1
    while(i<f):
        if(p%a==0):
            return False
        a+=1
    return True

def Cdiv(n):
    p=2
    sum=1
    while(n!=1):
        a=0
        while(checkPrime(p) and n%p==0):
            n=n/p
            a+=1
        sum=sum*(a+1)
        p+=1
    return sum

while(c<500):
    n+=i
    c=Cdiv(n)
    if(c>100):
        print(i,n,c)
    i+=1

