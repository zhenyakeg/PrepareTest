__author__ = 'student'
#N = int(input())
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
    A[s] = A.get(s,0) + 1
    s = get_next()
A = sorted(A.items(), key=lambda x: x[1], reverse=True)
k1 = 1
#k2 = 1
#j = 1
if len(A) == 1:
    k1 = 1
    k2 = 0
else:
    for i in range (len(A)-1):
        if A[0][1] == A[i+1][1]:
            k1 += 1
            #j +=1
        #elif A[j][1] == A[i+1][1] and i+1 != j:
            #k2 += 1
print(*A[0:k1][0])







# while A[i][1] == A[i+1][1]:
#     k1+=1
#     A = A[i::]
#
#
#
#
#
#
#
#
# if len(A) > 2:
#     k2 = 1
#     while A[i + 1][1] == A[i + 2][1]:
#         k2 += 1
#         A.pop(A[i])
# else:
#     k2 =0
