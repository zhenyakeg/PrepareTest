s = list(map(int,input().split()))
X, K = s[0], s[1] + 1
def Generation(X,k):
    n = X//5
    S = [[1]*(n+1) for i in range(k+1)]
    for k in range(2, k+1):
        for p in range (1, n+1):
            S[k][p] = S[k-1][p] + S[k][p-1]
    return (S[k][n])
print(Generation(X,K))
