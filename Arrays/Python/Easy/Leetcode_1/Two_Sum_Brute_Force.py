from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if "__main__" == __name__:
    nums = [1, 2]
    target = 3
    print(Solution().twoSum(nums, target))