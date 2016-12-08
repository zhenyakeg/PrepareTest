__author__ = 'student'

x = int(input())
def Transition(x , k):
    Output = [str(i) for i in range(10)] + [chr(65+i) for i in range(26)]
    z = x
    s = ''
    if z == 0:
        return '0'
    while z != 0:
        i = z%k
        s += Output[i]
        z//=k
    return s[::-1]
print(Transition(x,17).count('G'))
