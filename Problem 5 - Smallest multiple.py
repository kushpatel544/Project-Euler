#URL - https://projecteuler.net/problem=5

import math
#  using brute force
def isDiv(n):
    for x in range(1,21):
        if(n%x!=0):
            return False
    return True

n=2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
for x in range(100,n,10):
    print(x)
    if(isDiv(x)):
        print(x)
        break
    x-=1


"""
#using LCM(a,b)=a*b/gcd(a,b)
s=1
for x in range(1,21):
    s=s*x//math.gcd(x,s)
print(str(s))
"""