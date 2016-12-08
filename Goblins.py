__author__ = 'student'
In = list(map(int,input().split()))
def Bubble_sort_count(In):
    C = [0]*len(In)
    D = [[In[i],C[i]] for i in range(len(In))]
    n=len(D)
    m=n-1
    while m>0:
        for i in range(m):
            if (D[i][0] > D[i+1][0]):
                D[i],D[i+1] = D[i+1], D[i]
                D[i][1] += 1
                D[i+1][1] += 1
        m=m-1

    return D
P = Bubble_sort_count(In)
for i in range(len(P)-1):
    for k in range(1,len(P)-i-1):
        if P[i][0] == P[i+k][0]:
            P[i][1] += P[i+k][1]
            P.pop(i+k)


Out = ['%d:%d' % tuple(x) for x in P]
print(*Out)