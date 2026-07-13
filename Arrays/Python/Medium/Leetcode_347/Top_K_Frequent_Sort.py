from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_items[:k]]





if __name__ == "__main__":
    # Create an instance of the Solution class to call the topKFrequent method
    solution = Solution()

    # TEST CASE 1: Find top 2 frequent elements in [1,1,1,2,2,3]
    result1 = solution.topKFrequent([1,1,1,2,2,3], 2)
    print(f"Test 1 - nums=[1,1,1,2,2,3], k=2: {result1}")

    # TEST CASE 2: Find top 1 frequent element in [1]
    result2 = solution.topKFrequent([1], 1)
    print(f"Test 2 - nums=[1], k=1: {result2}")

    # TEST CASE 3: Find top 2 frequent elements in [4,1,1,1,2,2,3]
    result3 = solution.topKFrequent([4,1,1,1,2,2,3], 2)
    print(f"Test 3 - nums=[4,1,1,1,2,2,3], k=2: {result3}")