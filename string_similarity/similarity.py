import sys

def similaritySum(string):
    simSum = 0
    strLen = len(string)
    
    # try all suffixes
    for i in range(strLen):
        misMatch = False
        
        for j in range(strLen - i):
            if string[j] != string[i + j]:
                simSum += j
                misMatch = True
                break
            
        if not misMatch:
            simSum += strLen - i
        
    return simSum

if __name__ == '__main__':
    nbLines = int(sys.stdin.readline())
    
    for i in range(nbLines):
        line = sys.stdin.readline().strip()
        print(similaritySum(line))
