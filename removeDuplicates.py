class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0
        i=0
        while(i<len(nums)):
            if nums[i] ==nums[i-1]:
                nums.remove(nums[i])
            else:
                i+=1
        k=len(nums)       
        return k
