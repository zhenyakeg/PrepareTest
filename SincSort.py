def SincSort(A, B):
    D = tuple(zip(A,B))
    D = sorted(D, key=lambda x: x[1])
    for i in range (len(D)-1):
        k = 1
        s = 0
        while i+k < len(D) and D[i][1] == D[i+k][1]:
            k+=1
            s+=1
        if s > 0:
            D[i:i+k:1] = sorted(D[i:i+k:1], key=lambda x: x[0])
            s = 0
    return D

A = list(map(int,input().split()))
B = list(map(int,input().split()))
D = SincSort(A, B)
A = [a[0] for a in D]
B = [a[1] for a in D]
print(*A)
print(*B)