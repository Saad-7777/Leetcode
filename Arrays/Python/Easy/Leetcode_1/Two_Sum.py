from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []



if "__main__" == __name__:
    solution = Solution()
    nums = [2, 11, 7, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]