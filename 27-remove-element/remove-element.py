# two-pointers
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # sort first
        # use pointer to scan the sorted nums
        # append val into new array if not present in sorted nums
        # return len new array
        result = []
        # nums.sort()
        fastidx = 0
        while fastidx < len(nums):
            if val != nums[fastidx]:
                result.append(nums[fastidx])
            fastidx += 1
        nums[:] = result
        print(nums)
        return len(result)