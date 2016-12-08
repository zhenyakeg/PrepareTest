__author__ = 'student'
#import sys

#A = list(map(int, sys.stdin.read().split()))
def get_next():
    get_next.seed = (get_next.seed*513+1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2+3*get_next.seed)%999+1
    get_next.seed = int(input())

x = get_next()
M = 0
k = 0
ID = []
while x != 0:
    if x > M:
        M = x
        ID = [k]
    elif x == M:
        ID += [k]
    x = get_next()
    k += 1
print(*ID)