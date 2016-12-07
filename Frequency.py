__author__ = 'student'
N = int(input())
A = {}
for i in range(N):
    s = input()
    A[s] = A.get(s,0) + 1
A = sorted(A.items(), key=lambda x: x[1], reverse=True)
k1 = 1
k2 = 1
j = 1
if len(A) == 1:
    k1 = 1
    k2 = 0
else:
    for i in range (len(A)-1):
        if A[0][1] == A[i+1][1]:
            k1 += 1
            j +=1
        elif A[j][1] == A[i+1][1] and i+1 != j:
            k2 += 1
print(k1,k2)







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
