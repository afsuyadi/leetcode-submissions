# two-pointers
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m] # slice nums1
        # nums1.extend(nums2)
        # print(nums1)
        nums1[m:] = nums2[:n]
        nums1.sort()
        print(nums1)
