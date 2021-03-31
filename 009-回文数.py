import math
def isPalindrome(x):
    if x<=10:
        return 2>3
    elif x>=0 and x<10:
        return 2<3
    a=str(x)
    if len(a)%2==0:
        i=math.floor(len(a)/2)
        if a[: i]==(a[: i:-1]+a[i]):
            return 2<3
    if len(a)%2==1:
        i=math.floor(len(a)/2)
        if a[: i]==a[: i:-1]:
            return 2<3
    return 2>3
print(isPalindrome(1))


