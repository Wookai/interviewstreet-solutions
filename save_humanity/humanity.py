import sys

def findMatches(patient, virus):
    if len(virus) > len(patient):
        return 0
    
    foundMatch = False
    
    # try all possible starting positions for the virus
    for startPos in range(len(patient) - len(virus) + 1):
        hadError = False
        allMatch = True
        
        # check if rest of string matches
        for i in range(len(virus)):
            if patient[startPos + i] != virus[i]:
                if not hadError:
                    hadError = True
                else:
                    allMatch = False
                    break
                
        if allMatch:
            if foundMatch:
                sys.stdout.write(' ')
            else:
                foundMatch = True
            sys.stdout.write(str(startPos))
    
    sys.stdout.write('\n')

# read number of samples
N = int(sys.stdin.readline())

for i in range(N):
    # read data
    patient = sys.stdin.readline().strip()
    virus = sys.stdin.readline().strip()
    
    # skip blank line after sample
    sys.stdin.readline()
    
    findMatches(patient, virus)
