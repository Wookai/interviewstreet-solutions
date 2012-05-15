import sys

charMap = {'ab': 'c', 'ba':'c', 'bc':'a', 'cb':'a', 'ac':'b', 'ca':'b' }

# reduce the string by replacing pair of chars starting at position pos
def reduceString(s, pos):
    s2 = s[:pos]
    s2 += charMap[s[pos:pos+2]]
    s2 += s[pos+2:]
    return s2

def reduction(s):
    while True:
        # count number of each letter
        nbA = len([x for x in s if x == 'a'])
        nbB = len([x for x in s if x == 'b'])
        nbC = len([x for x in s if x == 'c'])
        
        nbTot = len(s)
        
        # we cannot reduce anymore if all chars are the same
        if nbA == nbTot or nbB == nbTot or nbC == nbTot:
            return nbTot
        
        # find most frequent char
        char = 'b'
        if nbA >= nbB and nbA >= nbC:
            char = 'a'
        elif nbC >= nbA and nbC >= nbB:
            char = 'c'
            
        # find first occurrence of char that has a different neighbor
        i = 0
        while i < len(s):
            if s[i] == char:
                if i > 0 and s[i - 1] != char:
                    s = reduceString(s, i - 1)
                    break
                elif i < nbTot and s[i + 1] != char:
                    s = reduceString(s, i)
                    break
            i += 1

if __name__ == '__main__':
    nbLines = int(sys.stdin.readline())
    for i in range(nbLines):
        line = sys.stdin.readline().strip()
        print(reduction(line))
