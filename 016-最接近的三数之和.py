def threeSumClosest(nums, target):
    b = sorted( nums )
    result = None
    for i in range( len( b ) ):
        chazhi = target - b[i]
        j = i + 1
        k = len(b) - 1
        if j >= k:
            break
        while( j < k ):
            if b[j] + b[k] < chazhi:
                if i + 1 == j and i == 0 and k == len(b) - 1:
                    result = b[i] + b[j] + b[k]
                    tempresult = result
                else:
                    tempresult = b[j] + b[k] + b[i]
                    if abs(tempresult - target) <= abs(result - target):
                        result = tempresult
                j = j + 1
                continue
            elif b[j] + b[k] == chazhi:
                return target
            else:
                if k == len(b) - 1 and i == 0 and i + 1 == j:
                    result = b[i] + b[j] + b[k]
                    tempresult = result
                else:
                    tempresult = b[j] + b[k] + b[i]
                    if abs(tempresult - target) <= abs(result - target):
                        result = tempresult
                k = k - 1
                continue
    return result
#print(threeSumClosest([1,2,-1,-4],1))
#print(threeSumClosest([0,1,2],3))
print(threeSumClosest([1,2,5,10,11],12))