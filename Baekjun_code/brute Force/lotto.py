import itertools
while True:
    string = list(map(int,input().split(" ")))
    k = string.pop(0)
    if k==0:
        break
    numSet = string
    res = itertools.combinations(numSet,6)
    for set in list(res):
        print(*set)
    print()