import math
import os
import random
import re
import sys

n=int(input())
if(n%2)==0:
    if(6<n<=20):
        print(n,"Weird")
    if(2<n<5 or n>20):
        print(n,"Not Weird")
else:
    print(n,"Weird")
