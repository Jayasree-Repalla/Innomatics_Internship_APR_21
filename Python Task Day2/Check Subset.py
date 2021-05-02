num=int(input())
for i in range(num):
    m=input()
    n=set(input().split())
    m1=int(input())
    n1=set(input().split())
    print(n.issubset(n1))