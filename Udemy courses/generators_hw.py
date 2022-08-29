def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)

import random

def rand_num(low,high,n):
    for i in range(n):
        i = random.randint(low,high)
        yield i

for num in rand_num(1,10,12):
    print(num)


s = 'hello'
s_iter = iter(s)

for i in s_iter:
    print(i)