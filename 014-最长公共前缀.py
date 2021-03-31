def longestCommonPrefix(strs):
    if len(strs)==0:
        return ''
    if len(strs)==1:
        return strs[0]
    M=min(strs)
    i=0
    j=1
    k=len(M)
    while(j<=k):
        if strs[i].startswith(M[0:j]):
            i=i+1
            if i==len(strs):
                i=0
                j=j+1
            continue
        else:
            break
    if j==0:
        return ''
    else:
        return M[0:(j-1)]
a=["dog","racecar","car"]
print(longestCommonPrefix(a))
