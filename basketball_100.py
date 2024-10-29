mod = 1_000_000_007

from functools import lru_cache

@lru_cache(None)
def solve(score1, score2):
    ways = 0
    if (score1==0 and score2==0):
        return 1
    
    if (score1 >=3):
        ways += solve(score1 - 3, score2)

    if (score2 >=3):
        ways += solve(score1, score2-3)

    if (score1 >=2):
        ways += solve(score1-2, score2)

    if (score2 >=2):
        ways += solve(score1, score2-2)
    
    ways %= mod
    return ways

n,m = list(map(int, input().strip().split())) 

print(solve(n,m))