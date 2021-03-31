def myAtoi(s):
    if s=='':
        return 0
    if len(s)==1 and s[0]<=chr(57) and s[0]>=chr(48):
        return int(s)
    elif len(s)==1:
        return 0
    s=s.lstrip()
    if (s[0]>chr(57) or s[0]<chr(48)) and s[0]!=chr(43) and s[0]!=chr(45):
        return 0
    else:
        for i,val in enumerate(s[1:]):
            if s[i+1]>chr(57) or s[i+1]<chr(48):
                i=i-1
                break
        if s[i+1]<=chr(57) and s[i+1]>=chr(48):
            i=i+1
            a=int(s[:i]+s[i])
            print(a)
            if a>(2**31-1):
                return 2**31-1
            elif a<-2**31:
                return -2**31
            else:
                return a
        else:
            return 0
# print(myAtoi('-4wwww+-42'))
# print(myAtoi('-+4wwww+-42'))
# print(myAtoi('4wwww+-42'))
# print(myAtoi('-9999999999999999999'))
# print(myAtoi('-+442'))
# print(myAtoi('-442'))
# print(myAtoi(''))
# print(myAtoi('1'))
# print(myAtoi('-'))
print(myAtoi('+1'))
# print(myAtoi('a'))