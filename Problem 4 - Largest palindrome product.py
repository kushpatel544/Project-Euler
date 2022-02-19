#URL - https://projecteuler.net/problem=4
n = 0
for p1 in range(999, 100, -1):
    for p2 in range(p1, 100, -1):
        x = p1 * p2
        if x > n:
            s = str(p1 * p2)
            if s == s[::-1]:
                n = p1 * p2
print(n)


    


