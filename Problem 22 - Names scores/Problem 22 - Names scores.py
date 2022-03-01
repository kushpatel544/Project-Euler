#URL - https://projecteuler.net/problem=22
f = open("Problem 22 - Names scores/p022_names.txt", "r")
s=[]
for x in f:
    s+=x.split(",")
for x in range(len(s)):
    s[x]=s[x].replace('"','')
s.sort()
score = 0
for x in s:
    sum=0
    for i in x:
        sum+=(ord(i)-ord('A'))+1
    score=score+sum*(s.index(x)+1)
print(score)





