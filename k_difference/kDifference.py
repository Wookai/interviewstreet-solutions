import sys

# read N and K
firstLine = sys.stdin.readline().strip().split(' ')
N = int(firstLine[0])
K = int(firstLine[1])

# read numbers
numbers = [int(x) for x in sys.stdin.readline().strip().split(' ')]

hashMap = {}
for n in numbers:
    # for each number, compute its two "differences"
    hashMap[n+K] = hashMap.get(n+K, 0) + 1
    hashMap[n-K] = hashMap.get(n-K, 0) + 1

count = 0
for n in numbers:
    # count how many numbers are the "difference" of another
    count += hashMap.get(n, 0)

# each pair has been counted twice, so divide by two
print(count/2)