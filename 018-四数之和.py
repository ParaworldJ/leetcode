def fourSum(nums, target):
    SXnum = sorted(nums)
    result = []
    for i in range(len(SXnum)):
        if i + 3 == len(SXnum):
            break
        Ftarget = target - SXnum[i]
        j = i + 1
        while(j + 2 < len(SXnum)):
            y = j + 1
            z = len(SXnum) - 1
            Starget = Ftarget - SXnum[j]
            while (y < z):
                if Starget - SXnum[y] - SXnum[z] == 0:
                    if [SXnum[i],SXnum[j],SXnum[y],SXnum[z]] not in result:
                        result = result + [[SXnum[i],SXnum[j],SXnum[y],SXnum[z]]]
                    y = y + 1
                    continue
                elif Starget - SXnum[y] - SXnum[z] < 0:
                    z = z - 1
                elif Starget - SXnum[y] - SXnum[z] > 0:
                    y = y + 1
            j = j + 1
    return result
# print(fourSum([1,0,-1,0,-2,2],0))
print(fourSum([-3,-2,-1,0,0,1,2,3],0))