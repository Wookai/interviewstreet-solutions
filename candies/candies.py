import sys
import numpy as np

def nbCandies(scores, N):
    candies = np.ones(N, dtype=int)
    
    changed = True
    while changed:
        changed = False
        for i in range(N):
            if i > 0 and scores[i - 1] < scores[i] and candies[i - 1] >= candies[i]:
                candies[i] = candies[i - 1] + 1
                changed = True
                
            if i < N - 1 and scores[i + 1] < scores[i] and candies[i + 1] >= candies[i]:
                candies[i] = candies[i + 1] + 1
                changed = True
    
    return np.sum(candies)

# read number of kids
N = int(sys.stdin.readline())

scores = []
for _ in range(N):
    # read data
    scores.append(int(sys.stdin.readline().strip()))

print(nbCandies(scores, N))