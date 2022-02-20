#URL - https://projecteuler.net/problem=9
n=1000
for a in range(1,n//2):
    for b in range(a,n//2):
        c=n-a-b
        if(a*a+b*b==c*c):
            print(a,b,c,a*b*c)
            break
