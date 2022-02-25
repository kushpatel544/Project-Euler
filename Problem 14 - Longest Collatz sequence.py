#URL - https://projecteuler.net/problem=14


m = 0
mSeq = 0
def Cseq(n):
    c=0
    while(n!=1):
        if(n%2==0):
            n=n//2
        else:
            n=3*n+1
        c+=1
    return c+1
i=2
while(i<=1000000):
    l=Cseq(i)
    if(l>mSeq):
        mSeq=l
        m=i
        print("MAX: ",m,mSeq)
    i+=1

