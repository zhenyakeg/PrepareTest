__author__ = 'student'
A = []
s = list(map(int,input().split()))
while s != [0,0]:
    A.append(s)
    s = list(map(int,input().split()))
k = 0
for p in A:
    if p[0] % 2 == 0 and p[1] % 7 == 0 and (len(str(p[0])) >= 3 or len(str(p[1])) >= 3):
        k+=1
print(k)