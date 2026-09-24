class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num: # 3, 2, 3
                count += 1
            else:
                count -= 1
        return candidate
        
    