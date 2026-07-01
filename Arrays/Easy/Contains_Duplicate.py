from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 3]))  # Expected: True
    print(sol.hasDuplicate([1, 2, 3, 4]))  # Expected: False
    print(sol.hasDuplicate([1, 1, 2, 3]))
