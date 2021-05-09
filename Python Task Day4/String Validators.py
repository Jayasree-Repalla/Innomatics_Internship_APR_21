if __name__ == '__main__':
    s = input()
    l,m,n,o,p=0,0,0,0,0
    for i in s:
        if (i.isalnum()):
           print("True")
           break
        else:
            l=l+1
            if l==len(s):
               print("False")
    for i in s:
        if (i.isalpha()):
           print("True")
           break
        else:
            m=m+1
            if m==len(s):
               print("False")
    for i in s:
        if (i.isdigit()):
           print("True")
           break
        else:
            n=n+1
            if n==len(s):
               print("False")
    for i in s:
        if (i.islower()):
           print("True")
           break
        else:
            o=o+1
            if o==len(s):
               print("False")
    for i in s:
        if (i.isupper()):
           print("True")
           break
        else:
            p=p+1
            if p==len(s):
              print("False")