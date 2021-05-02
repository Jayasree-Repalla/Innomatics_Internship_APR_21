def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4)==0:
        print("true")
    else:    
        return leap
year = int(input())
print(is_leap(year))