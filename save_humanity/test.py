import sys
import random

N = int(sys.argv[1])
method = sys.argv[2]

sum = 0

if method == 'range':
    print('range')
    for i in range(N):
        sum += random.randint(1, 10)
else:
    print('while')
    i = 0
    while i < N:
        sum += random.randint(1, 10)
        i += 1