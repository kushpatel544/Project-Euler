#URL - https://projecteuler.net/problem=19
import datetime

d30=[4,6,9,11]
d31=[1,3,5,7,8,10,12]
y=1900
c,sum=0,0

def Ndays(m,y): #return Number of days in a month
    if m in d30:
        return 30
    if m in d31:
        return 31
    if m==2:
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            return 29
        else:
            return 28

for i in range(1900,2001):
    for j in range(1,13):
        if(c==1 and i>1900):
           sum+=1
        days=Ndays(j,i)
        while(c<=days):
            c+=7
        c=c%days
                
print(sum)

########### USING datetime library
#sdays=0
# for y in range(1901, 2001):
# 	    for m in range(1, 13):
# 	        if datetime.date(y, m, 1).weekday() == 6:
# 	            sdays+=1
# print(sdays)
    