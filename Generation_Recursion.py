def generation(X,K):
    if X == 0 or K == 1:
        return 1
    n = 0
    for i in range (X+1):
        n+=generation(X-i, K-1)
    return n
Sum = int(input())
K = int(input())
print(generation(Sum//5,K))

