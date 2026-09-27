class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}
        for i in range(len(nums)):
            idx_exist = last_seen.get(nums[i], None)
            # print("i, idx_exist=", i, idx_exist)
            if idx_exist != None and abs(i - idx_exist) <= k:
                return True
            else:
                last_seen[nums[i]] = i
        # print("LAST SEEN", last_seen)
        return False
