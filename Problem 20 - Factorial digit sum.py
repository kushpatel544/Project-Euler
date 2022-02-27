#URL - https://projecteuler.net/problem=20

import math

n=str(math.factorial(100))
ans = sum(int(x)
for x in n)
print(ans)