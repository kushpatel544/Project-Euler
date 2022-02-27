#URL - https://projecteuler.net/problem=21

a,b,sum=0,0,0
s=[]
def d(n):
    sdiv = 0
    for i in range(1,n):
        if(n%i==0):
            sdiv+=i
    return sdiv

for x in range(1,10001):
    a=d(x)
    b=d(a)
    if(x==b and a!=b and a not in s):
        s.append(x)
        sum=sum+x+a
        print(x,a)
print(sum)

