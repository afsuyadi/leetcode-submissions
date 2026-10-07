# two-pointers
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort() # sort first, zero will be in the front
        # # [0,0,1,3,12]
        # # lastzeroidx = 1
        # lastzeroidx = 0
        # # print(len(nums))
        # for i, num in enumerate(nums):
        #     print(num)
        #     if num != 0:
        #         print('i=', i)
        #         lastzeroidx = i-1
        #         break
        # print('lastzeroidx',lastzeroidx)
        # print('before', nums)
        # print('nums[0:lastzeroidx+1]', nums[0:lastzeroidx+1])
        # nums[len(nums):] = nums[0:lastzeroidx+1]
        # # nums = nums[lastzeroidx+1:]
        # print('after', nums)
        # for i in range(lastzeroidx+1): # 0, 1
        #     nums.pop(0)
        #     print('pop i=', i)
        # print('final', nums)
        
        # slowidx = 0
        zeroidx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroidx] = nums[zeroidx], nums[i]
                zeroidx += 1