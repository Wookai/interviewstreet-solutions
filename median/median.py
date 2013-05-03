import sys

values, N = [], 0

def printMedian():
    global values, N
    
    if N == 0:
        print 'Wrong!'
    elif N == 1:
        print values[0]
    elif N % 2 == 0:
        val = (values[N / 2 - 1] + values[N / 2]) / 2.0
        if int(val) == val:
            val = int(val)
        print val
    else:
        print values[N / 2]

def applyOp(operation, value):
    global values, N
    
    if operation == 'a':
        i = 0
        while i < N and values[i] < value:
            i += 1
        values.insert(i, value)
        N += 1
    elif N > 0:
        try:
            values.remove(value)
            N -= 1
        except:
            pass

# read number of operations
M = int(sys.stdin.readline())

for _ in range(M):
    # read data
    data = sys.stdin.readline().strip().split(' ')
    operation = data[0]
    value = int(data[1])
    
    applyOp(operation, value)
    printMedian()