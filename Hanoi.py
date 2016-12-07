def Hanoi(n,i=1,k=2):
    if (i == 2 and k == 3) or (i == 3 and k == 2):
        tmp = 6- i- k
        Hanoi(n,i,tmp)
        Hanoi(n,tmp,k)

    else:
        if n==1:
            print (n, i, k)
        else:
            tmp = 6 - i -k
            Hanoi(n-1, i, tmp)
            print (n, i, k)
            Hanoi(n-1, tmp, k)
Hanoi(int(input()))
