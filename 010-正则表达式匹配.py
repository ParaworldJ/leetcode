# from collections import defaultdict
# def isMatch(s, p):
#     if p[0]=='*':
#         return False
#     if len(s)==1: 
#         if s[0]==p[0] or s[0]=='.':
#             return True
#         else:
#             return False
#     if p=='' or p=='.*':
#         return True
#     flag=0
#     temp=p
#     Tp=defaultdict(list)
#     i,j,k=0,0,0
#     d=[]
#     #i用来记s j用来记字典
#     while(temp):
#         if len(temp)>1 and temp[1]=='*':
#             if flag==0 and i!=0:
#                 j=j+1
#             flag=1
#         else:
#             if i!=0:
#                 j=j+1
#             flag=0
#         if flag==1:
#             if(temp[0]=='.'):
#                 k=k+1
#             Tp[j].append(temp[0]+temp[1])
#             temp=temp[2:]
#         else:
#             if temp[0]=='*':
#                 return false
#             Tp[j].append(temp[0])
#             temp=temp[1:]
#         i=i+1
#     i,j=0,0
#     #k记录有几个.*,
#     zf=[]
#     t,t1,flag1=0,0,0
#     Tp2=defaultdict(list)
#     if k>0:
#         while(bool(Tp)):
#             if '*' in Tp[t][0]:
#                 if flag1!=0:
#                     t1=t1+1
#                 Tp2[t1]=Tp[t]
#                 t1=t1+1
#             else:
#                 if t1 in Tp2:
#                     Tp2[t1][0]=Tp2[t1][0]+Tp[t][0]
#                 else:
#                     Tp2[t1].append(Tp[t][0])
#                 zf=zf+[t1]
#                 flag1=1
#             del Tp[t]
#             t=t+1
#         for key in Tp2:
#             if '.*' in Tp2[key]:
#                 d=d+[key]
#                 print(d)
#         l=len(Tp2)-1
#         zf=list(set(zf)) #字符串的位置
#         d=list(set(d))  #记录.*的位置
#         if d[-1]==l and d[0]!=0:
#             while(i<len(s)):
#                 if i in d:
                    
#                     pass   
#                 elif i in zf:
#                     if s.startswith(Tp2[j][0],i):
#                         j=j+1
#                         i=i+len(Tp2[j][0])
#                         continue
#                     elif i==0 or len(Tp2[j][0])>len(s[i:]):
#                         return False
#                     else:
#                         i=i+1
#                     pass
#                 else:
#                     pass
#         elif d[-1]!=l and d[0]==0:

#             return 2
#         elif d[-1]==l and d[0]==0:

#             return 3
#     i,j=0,0
#     while(s and bool(Tp)):
#         if s[0] in Tp[i][j] or '.' in Tp[i][j]:
#             if '*' in Tp[i][j]:
#                 if len(Tp)>1:
#                     if Tp[i+1][0]==s[0] or Tp[i+1][0]=='.':
#                         for m in range(len(s)):
#                             if s[m]!= s[0]:
#                                 break
#                         m=m+1
#                         n=1
#                         while(n<=(len(Tp)-1)):
#                             if Tp[n+i][0]!=s[0] and Tp[n+i][0]!='.':
#                                 break
#                             n=n+1
#                         n=n-1
#                         if n>m:
#                             return False
#                         else:
#                             del Tp[i]
#                             while(n):
#                                 del Tp[i+n]
#                                 n=n-1
#                             s=s.lstrip(s[0])
#                             j=0
#                             continue
#                     else:
#                         s.lstrip(s[0])
#                         del Tp[i]
#                         j=0
#                         i=i+1
#                         continue
#                 else:
#                     del Tp[i]
#                     s=s.lstrip(s[0])
#                     j=0
#                     continue
#             else:
#                 s=s[1:]
#                 del Tp[i]
#                 i=i+1
#                 j=0
#                 continue
#         else:
#             if '*' in Tp[i][j]:
#                 if j<len(Tp[i]):
#                     j=j+1
#                     continue
#                 else:
#                     del Tp[i]
#                     j=0
#                     continue
#             else:
#                 return False
#     if s=='' and bool(Tp)==False:
#         return True
#     else:
#         if '.*' in Tp[l]:
#             return True
#         return False 
def isMatch(s, p):
    column=len(s)+1
    line=len(p)+1
    a=[[0]*(line) for i in range(column)]
    if p==s:
        return True
    if p=='' or p[0]=='*':
        return False
    for i in range(column):
       for j in range(line):
            if i==0:
                if j==0:
                    a[0][0]='T'
                else:
                    if p[j-1]=='*':
                        a[0][j]=a[0][j-2]
                    else:
                        a[0][j]='F'
            else:
                if j==0:
                    a[i][0]='F'
                else:
                    if s[i-1]==p[j-1] or p[j-1]=='.':
                        a[i][j]=a[i-1][j-1]
                    else:
                        a[i][j]='F'
                    if p[j-1]=='*':
                        if a[i][j-2]=='T':
                            a[i][j]='T'
                        else:
                            if s[i-1]==p[j-2] or p[j-2]=='.':
                                if a[i-1][j]=='T':
                                    a[i][j]='T'
                                else:
                                    a[i][j]='F'
                            else:
                                a[i][j]='F'
    i=0
    if a[len(s)][len(p)]!='T':
            return False
    j=len(s)
    i=len(p)
    while(j>1):
        if a[j-1][i-1]=='T':
            j=j-1
            i=i-1
        elif a[j-1][i]=='T':
            j=j-1
        elif a[j][i-1]=='T':
            i=i-1
        elif p[i-1]=='*':
            if a[j][i-2]=='T':
                i=i-2
            else:
                return False
        else:
            return False
    return True
       
# print(isMatch('aab','c*a*b'))
print(isMatch('aaa','ab*ac*a'))
# print(isMatch('aa','a'))
# print(isMatch('ab','.*c'))
# print(isMatch('abc','abc*a*d*'))        
# print(isMatch('ab','abc.*.*a*a.*'))
# print(isMatch('ab','.*abc.*.*a*a.*'))
# print(isMatch('aaa','aaa*'))