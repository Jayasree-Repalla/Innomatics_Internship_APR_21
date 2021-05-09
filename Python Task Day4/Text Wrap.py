import textwrap

def wrap(string, max_width):
    l=textwrap.wrap(string,max_width)
    str1=''
    for i in l:
        str1=str1+i+"\n"
    return str1