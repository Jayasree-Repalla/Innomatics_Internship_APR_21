n1=int(input())
myset=set(input().split())

n2=int(input())
myset1=set(input().split())

myset3=myset.difference(myset1)
print(len(myset3))