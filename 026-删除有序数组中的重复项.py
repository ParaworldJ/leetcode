class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 1
        while(i < len(nums)):
            if nums[i] == nums[i-1]:
                del(nums[i])
            else:
                i = i + 1
        l = len(nums)
        return l