__author__ = 'student'
N = int(input())
S = [0, 0, 0]
l = float('+inf')
C = [[l, l, l], [l, l, l], [l, l, l]]
for i in range (N):
    C.append(list(map(int, input().split())))
    S.append(min(S[i+2] + C[i+3][0], S[i+1]+ C[i+2][1], S[i]+C[i+1][2]))
print(S[N+2])
