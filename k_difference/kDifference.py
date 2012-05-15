import sys
import math

firstLine = sys.stdin.readline().strip().split(' ')
N = int(firstLine[0])
K = int(firstLine[1])

numbers = [int(x) for x in sys.stdin.readline().strip().split(' ')]
map = {}
for n in numbers:
    print(n+K, n-K)
    map[n+K] = 1
    map[n-K] = 1

count = 0
for n in numbers:
    for k in map.keys():
        if k == n:
            count += 0.5

print(count)