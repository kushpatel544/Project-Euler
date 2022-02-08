#URL: https://projecteuler.net/problem=2
a=1
b=2
c=a+b
sum=2
while(c<4000000):
    a=b
    b=c
    c=a+b
    if(c%2==0):
        sum+=c
print(sum)
