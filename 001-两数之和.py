from collections import defaultdict
def twoSum1(nums,target):
    a=defaultdict(list)
    i=0
    for j in nums:
        a[j].append(i)
        i=i+1
    for key in a:
        if ((target-key) in a.keys()): 
            if ((target-key)!=key):
                return a[key][0],a[target-key][0]
            elif ((target-key)==key) and len(a[key])>1:
                return a[key][0],a[key][1]
            
    return 0,0

def twoSum(nums, t) :
    a = {}
    for idx in range(len(nums)) :
        if a.get(t - nums[idx]) is None : a[nums[idx]] = idx
        else : return [idx, a[t - nums[idx]]]
print(twoSum([3,3],7))
