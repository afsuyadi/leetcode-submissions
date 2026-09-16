class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0 # fast pointer
        k = 1 # slow pointer
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1 # only progress when a not duplicated number is found
        return k