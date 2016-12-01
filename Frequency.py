__author__ = 'student'
N = int(input())
A = {}
for i in range(N):
    s = input()
    A[s] = A.get(s,0) + 1
A = sorted(A.items(), key=lambda x: x[0])
k1 = 1
k2 = 0
i = 0
while A[i][1] == A[i+1][1]:
    k1+=1
    A = A[i::]
    i+=1
while A[i+1][1] == A[i+2][1]:
    k2 += 1
    A.pop(A[i])