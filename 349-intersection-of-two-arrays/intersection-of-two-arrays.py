class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1dict = {}
        nums2dict = {}
        similar = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and num1 not in similar:
                    similar.append(num1)
        
        return similar