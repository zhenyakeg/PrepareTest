def price(N, P):
    Cost = [float('+inf'),P[0]]+[None]*(N-1)
    for i in range (2,N+1):
        Cost[i]= P[i-1] + min(Cost[i-2], Cost[i-1])
    return Cost[N]
N = int(input())
A = list(map(int, input().split()))
print(price(N,A))