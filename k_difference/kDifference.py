import sys

firstLine = sys.stdin.readline().strip().split(' ')
N = int(firstLine[0])
K = int(firstLine[1])

numbers = [int(x) for x in sys.stdin.readline().strip().split(' ')]

hashMap = {}
for n in numbers:
    hashMap[n+K] = hashMap.get(n+K, 0) + 1
    hashMap[n-K] = hashMap.get(n-K, 0) + 1

count = 0
for n in numbers:
    count += hashMap.get(n, 0)

print(count/2)