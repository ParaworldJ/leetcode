def reverse(x):
    s=str(x)
    elif x<0:
        a=s[0]+s[-1:0:-1]
    else:
         a=s[-1:0:-1]+s[0]
    if int(a)>(2**31-1) or int(a)<-2**31:
        return 0
    return int(a)
a=reverse(0)
print(a)