class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        collect = {}
        for num in nums:
            count = collect.get(num, 0) + 1
            print("NUM, COUNT:", num, count)
            if count > 1:
                return True
            collect[num] = count
        print("COLLECT:", collect)
        return False
    