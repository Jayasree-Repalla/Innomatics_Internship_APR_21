import re
n=int(input())
for i in range(n):
    n1=input()
    if(len(n1)==10):
        n2=(re.findall(r'^[7-9]\d{9}$',n1))
        if(len(n2)==1):
            print("YES")
        else:
           print("NO")
    else:
        print("NO")