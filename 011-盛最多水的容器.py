def maxArea(height):
    # if height==[]:
    #     return []
    # l=len(height)
    # max=0
    # for i, h in enumerate(height):
    #     j=i
    #     n=[k for k in range(len(height)) if height[k]>=h and k>i]
    #     if n!=[] and max<(h*(n[-1]-i)):
    #         max=h*(n[-1]-i)
    #     n=[k for k in range(len(height)) if height[k]<h and k>i]
    #     for j in range(len(n)):
    #         if max<(height[n[j]]*(n[j]-i)):
    #             max=height[n[j]]*(n[j]-i)
    # return max
################### 依旧是暴力算法##########
################### 使用双指针 #############
    if height==[]:
        return []
    i,j=0,len(height)-1
    a=height[0]*(j-i)
    b=height[-1]*(j-i)
    maxn= (height[0]>=height[-1] and [b] or [a])[0]
    while(i<j):
        ########### 序列解析式实际上还是遍历了一遍，还是等同于两个for超时
        # if height[i]>height[j]:
        #     # j=(lambda k : height[k]>height[j],height[j,i,-1] )[1][0]
        #     n=[k for k in range(j-1,i,-1) if height[k]>height[j] and k>i]
        #     if n==[]:
        #         return max
        #     else:
        #         n=n[0]
        #         j=n
        #         h=min(height[i],height[j])
                
        #         if  max<(j-i)*h:
        #             max=(j-i)*h
        # elif height[i]<=height[j]:
        #      # j=(lambda k : height[k]>height[j],height[j,i,-1] )[1][0]
        #      n=[k for k in range(i+1,j) if height[k]>height[i] and k<j]
        #      if n==[]:
        #          return max
        #      else:
        #          n=n[0]
        #          i=n
        #          h=min(height[i],height[j])
        #          print(n,i,j)
        #          if  max<(j-i)*h:
        #              max=(j-i)*h
        ans=min(height[i],height[j])*(j-i)
        maxn=max(ans,maxn)
        if height[i]>height[j]:
            j=j-1
        elif height[i]<=height[j]:
            i=i+1
    return maxn
height=[1,2,4,3]
height=[1,2,3,4,5,25,24,3,4]
print(maxArea(height))