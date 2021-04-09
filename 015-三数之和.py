
def threeSum(nums):
    # if len(nums)<3:
    #     return []
    # D=sorted(nums)
    # temp=None
    # f=1
    # g=[]
    # for i,j in enumerate(D):
    #     if j == temp:
    #         if f < 3:
    #             g = g + [j]
    #             f = f + 1
    #         else:
    #             continue
    #     else:
    #         f = 1
    #         temp = j
    #         g = g + [j]
    # print(g)
    # i = 0
    # target = 0
    # tempi = None
    # answer = []
    # while(i < (len(g) - 2)):
    #     if g[i] == tempi:
    #         i = i + 1
    #         continue
    #     else:
    #         tempi = g[i]
    #         targettemp = target - g[i]
    #         j = i + 1
    #         tempj = None
    #         while(j < (len(g) - 1)):
    #             if g[j] == tempj:
    #                 j = j + 1
    #                 continue
    #             else:
    #                 k = len(g) - 1
    #                 tempj = g[j]
    #                 tempk = None
    #                 while(k > j):
    #                     if g[k] == tempk:
    #                         k = k - 1
    #                         continue
    #                     else:
    #                         if (g[j] + g[k]) == targettemp:
    #                             answer = answer + [[g[i],g[j],g[k]]]
    #                             tempk=g[k]
    #                     k = k - 1
    #             j = j + 1
    #     i = i + 1
    if len(nums)<3:
        return []
    D=sorted(nums)
    temp=None
    f=1
    g=[]
    for i,j in enumerate(D):
        if j == temp:
            if f < 3:
                g = g + [j]
                f = f + 1
            else:
                continue
        else:
            f = 1
            temp = j
            g = g + [j]
    i = 0
    print(g)
    tempi = None
    answer=[]
    target = 0
    while(i < (len(g) - 2)):
        if g[i] == tempi:
            i = i + 1
            continue
        else:
            tempi = g[i]
            targettemp = target - g[i]
            j = i + 1
            k = len(g) - 1
            tempj, tempk = None, None
            while(j < k):
                while ( g[j] == tempj and (g[j] + g[k] == targettemp) ):
                    j = j + 1
                while ( g[k] == tempk and (g[j] + g[k] == targettemp) ):
                    k = k - 1 
                if g[j] + g[k] == targettemp:
                    answer = answer + [[g[i],g[j],g[k]]]
                    tempj = g[j]
                    tempk = g[k]
                    j = j + 1
                    k = k - 1
                elif g[j] + g[k] < targettemp:
                    tempj = g[j]
                    j = j + 1
                elif g[j] + g[k] > targettemp:
                    tempk = g[k]
                    k = k - 1
            i = i + 1
    return answer
# a=[-1,0,1,2,-1,-4,-1,-1,-1]
a=[1,2,-2,-1]
# a=[0,0,0,0,0,0,0,0,0]

# a=[-2,0,0,2,2]
print(threeSum(a))