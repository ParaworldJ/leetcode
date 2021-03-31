import math
def longestPalindrome(s):
    ######## 暴力解法，超时不可用##########
    # i,j=0,0
    # max=0
    # if s=='':
    #     return ''
    # longest=s[0]
    # while(i<(len(s)-1)):
    #     j=math.ceil((len(s)-i)/2)+i
    #     while(j>i):
    #         a=s[i:j]
    #         if (a+s[j-1:i:-1]+s[i]) in s:
    #             if len(a+s[j-1:i:-1]+s[i])>max:
    #                 max=len(a+s[j-1:i:-1]+s[i])
    #                 longest=a+s[j-1:i:-1]+s[i]
    #                 continue
    #         elif (a+s[j-2:i:-1]+s[i]) in s:
    #             if len(a+s[j-2:i:-1]+s[i])>max:
    #                 max=len(a+s[j-2:i:-1]+s[i])
    #                 longest=a+s[j-2:i:-1]+s[i]
    #                 continue
    #         j=j-1
    #     i=i+1
    # return longest
###############中心展开################
    Lstart,Lend=0,0
    left1,left2,right1,right2=0,0,0,0
    for i in range(len(s)):
        left1,right1=expand(s,i,i)
        if (i+1)<=(len(s)-1) and s[i]==s[i+1]:
            left2,right2=expand(s,i,i+1)
        if (right1-left1)>(Lend-Lstart):
            Lstart,Lend=left1,right1
        if (right2-left2)>(Lend-Lstart):
            Lstart,Lend=left2,right2
    return s[Lstart:Lend+1]
def expand(s,start,end):
    while(start>=0 and end<len(s) and s[start]==s[end]):
        start=start-1
        end=end+1
    return start+1,end-1

a=longestPalindrome('cbba')
print(a)