__author__ = 'student'
def get_next():
    get_next.seed = (get_next.seed*513+1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2+3*get_next.seed)%999+1
get_next.seed = int(input())

A = {}
s = get_next()
while s != 0:
    A[s] = A.get(s, 0) + 1
    s = get_next()
A = sorted(A.items(), key=lambda x: x[1], reverse=True)
k1 = 1
if len(A) == 1:
    k1 = 1
    k2 = 0
else:
    for i in range (len(A)-1):
        if A[0][1] == A[i+1][1]:
            k1 += 1
S = A[0:k1]
F = [p[0] for p in S]
print(*F)
