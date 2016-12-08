__author__ = 'student'
A = []
In = list(map(int,input().split()))
while In != [0,0]:
    A.append(In)
    In = list(map(int,input().split()))
k = 0
for p in A:
    if p[0] % 3 == 0 and p[1] % 2 == 0 or (p[0] % 9 == 0 and p[1] % 9 == 0):
        k+=1
print(k)