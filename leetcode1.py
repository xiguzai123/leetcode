from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l < 2:
            return []
        for i in range(l):
            n1 = nums[i]
            n2 = target - n1
            for j in range(l):
                if i == j:
                    continue
                n = nums[j]
                if n == n2:
                    return [i, j]
        return []
