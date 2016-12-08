def SincSort(V, M):
    D = list(zip(V,M))
    n=len(D)
    m=n-1
    while m>0:
        for i in range(n-1):
            if (D[i][0] >= D[i+1][0]):
                D[i],D[i+1] = D[i+1], D[i]
        m=m-1
    return D

A = list(map(int,input().split()))
B = list(map(int,input().split()))
D = SincSort(A, B)
B = [a[1] for a in D]
print(*B)

