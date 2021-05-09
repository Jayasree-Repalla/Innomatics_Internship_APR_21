import re
n=int(input()) 
for i in range(n): 
    k=input() 
    print (bool(re.match(r'^[+-]?\d*?\.{1}\d+$',k))) 