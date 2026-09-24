class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majorlen = len(nums) / 2
        collect = {}
        for num in nums:
            collect[num] = collect.get(num, 0) + 1
        for key, val in collect.items():
            if val >= majorlen:
                return key
        
    