__author__ = 'student'
Nums = []
Input = list(map(int,input().split()))
while Input != [0,0]:
    Nums.append(Input)
    Input = list(map(int,input().split()))
j = 0
for p in Nums:
    if p[0] % 3 == 0 and p[1] % 2 == 0 or (p[0] % 9 == 0 and p[1] % 9 == 0):
        j+=1
print(j)