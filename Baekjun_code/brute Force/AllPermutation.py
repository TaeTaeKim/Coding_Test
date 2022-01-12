from itertools import permutations
def solutnion():
    N= int(input())
    for i in permutations(range(1,N+1)):
        print(*i)
solutnion()