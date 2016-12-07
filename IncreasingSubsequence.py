def LAS_length(A):
    n = len(A)
    L = [0]*n
    for i in range (n):
        for j in range(i):
            if L[j] > L[i] and A[j] < A[i]:
                L[i] = L[j]
        L[i]+=1
A = [4,2,1,3,5,0]
print(LAS_length(A))