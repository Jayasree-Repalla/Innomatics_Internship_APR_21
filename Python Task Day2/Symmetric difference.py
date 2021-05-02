n=int(input())
myset=set(map(int,input().split()))
n1=int(input())
myset1=set(map(int,input().split()))

myset2=myset.difference(myset1)
myset3=myset1.difference(myset)

output=myset2.union(myset3)

for i in sorted(list(output)):
    print(i)