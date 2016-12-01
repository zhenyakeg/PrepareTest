__author__ = 'student'

import sys
s = sys.stdin.read().split()

n = int(s[0])
A = int(s[1], base=n)
k = int(s[2])
def Transition(x , k):
    Out = [str(i) for i in range(10)] + [chr(65+i) for i in range(26)]
    z = x
    s = ''
    if z == 0:
        return '0'
    while z != 0:
        i = z%k
        s += Out[i]
        z//=k
    return s[::-1]

print(Transition(A,k))
