#URL - https://projecteuler.net/problem=17

ones = {
    0: "", 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}

def Cword(n):
    if n==1000:
        return "onethousand"
    if n==100:
        return "onehundred"
    if n<20:
        return ones[n]
    if n<100:
        return tens[n//10]+ones[n%10]
    if n<1000:
        add=""
        if(n%100!=0):
            add="and"
        return ones[n//100]+"hundred"+add+Cword(n%100)

sum=0
for x in range(1,1001):
    print(Cword(x))
    sum+=len(Cword(x))
print(sum)
     