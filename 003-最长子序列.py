def lengthOfLongestSubstring(s):
    i,j=0,1
    max=0
    if len(s)==0:
        return 0
    elif len(s)==1:
        return 1
    else:
        while(j<len(s)):
            
            print('1:',s[i:j],j,s[j],max)
            if s[i:j].find(s[j])+1:
                i=i+s[i:j].index(s[j])+1
                print('2:',i,s.index(s[j]))                
            j=j+1
            if len(s[i:j])>max:
                max=len(s[i:j])    
        return s[i:j],max    
print(lengthOfLongestSubstring(''))