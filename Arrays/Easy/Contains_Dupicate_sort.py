from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 2, 1]))