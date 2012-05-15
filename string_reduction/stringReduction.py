import sys

cache = {}

def reduction(s):
    if s in cache.keys():
        return cache[s]
    
    minLen = len(s)
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            s2 = ''
            if i > 0:
                s2 = s[:i]
            s2 += chr(3 * 98 - ord(s[i]) - ord(s[i+1]))
            if i + 1 < len(s):
                s2 += s[i+2:]
            l = reduction(s2)
            if l < minLen:
                minLen = l
                
    cache[s] = minLen
    
    return minLen

if __name__ == '__main__':
    first = True
    nbLines = 0
    count = 0
    nbLines = int(sys.stdin.readline())
    for i in range(nbLines):
        line = sys.stdin.readline().strip()
        print(reduction(line))
