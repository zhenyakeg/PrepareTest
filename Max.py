__author__ = 'student'
import sys
A = list(map(int, sys.stdin.read().split()))
A = A[:A.index(0):]
M = 0
k = 0
for i in range(len(A)):
    if A[i] > M:
        M = A[i]
        k = 1
    elif A[i] == M:
        k+=1
print(k)