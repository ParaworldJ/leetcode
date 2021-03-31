import heapq
def findMedianSortedArrays(nums1 , nums2):
    a=sorted(heapq.merge(nums1,nums2))
    length=len(a)
    med=len(a)%2
    if length>0:
        if med==0:

            mednum=(a[int(len(a)/2)]+a[int(len(a)/2)-1])/2
        elif med==1:
            mednum=a[int((len(a)-1)/2)]
    else:
        return 0
    return mednum
a=findMedianSortedArrays([2],[])
print(a)