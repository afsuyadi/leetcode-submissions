class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # ====== 34 ms =====
        # similar = []
        # for num1 in nums1:
        #     for num2 in nums2:
        #         if num1 == num2 and num1 not in similar:
        #             similar.append(num1)
        
        # return similar
        
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        p1 = 0
        p2 = 0
        interaction = []
        while p1 < len1 and p2 < len2:
            if nums1[p1] == nums2[p2] and nums1[p1] not in interaction:
                interaction.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return interaction  