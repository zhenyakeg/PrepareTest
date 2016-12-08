__author__ = 'student'
def gen(N, pref =''):
    if N == 0:
        return pref + ' '
    for letter in '0','1':
        gen(N-1,pref+letter)
s = input().split()
N = int(s[0])
