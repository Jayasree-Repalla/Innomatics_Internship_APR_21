def count_substring(string, sub_string):
    n=0
    for i in range(len(string)):
        if(i+len(sub_string)<=len(string)):
          if(string[i:i+len(sub_string)]==sub_string):
            n=n+1
    return n