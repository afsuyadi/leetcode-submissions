# from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collection = {}
        idx = 0
        result = []
        for num in nums:
            # check if 3 is in collection
            diff = target - num
            if diff in collection: # 3 is in collection
                result.append(collection[diff])
                result.append(idx)
                
                # print(collection[diff], idx)
            else:
                collection[num] = idx
            idx += 1
            # print(collection)
                        
        return result