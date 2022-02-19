#URL: https://projecteuler.net/problem=1

######## FIRST SOLUTIION ###########
x=3
y=5
sum=0
while(x<1000):
    sum+=x
    x+=3
while(y<1000):
    if(y%3!=0):
        sum+=y
    y+=5
print(sum)
    
######## USING ARTHEMATIC SERIES #########
# last=999
# def func(n):
#     p=last//n
#     return n*(p*(p+1))/2
# print(int(func(3)+func(5)-func(15)))



