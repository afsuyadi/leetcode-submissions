class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # n = len(nums) # if len(nums) = 4,
        for num in range(len(nums)+1): # range(n) = [0,1,2,3]
            if num not in nums:
                return num
            
    