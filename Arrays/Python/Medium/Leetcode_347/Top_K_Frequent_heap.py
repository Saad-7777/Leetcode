from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Count the frequency of each number in nums
        count = Counter(nums)

        # Use a heap to find the k most frequent elements
        # heapq.nlargest returns the k largest elements based on the frequency
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    # Create an instance of the Solution class to call the topKFrequent method
    solution = Solution()

    # TEST CASE 1: Find top 2 frequent elements in [1,1,1,2,2,3]
    # Expected behavior: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
    # So the result should be [1, 2] (the two most frequent elements)
    result1 = solution.topKFrequent([1,1,1,2,2,3], 2)
    print(f"Test 1 - nums=[1,1,1,2,2,3], k=2: {result1}")

    # TEST CASE 2: Find top 1 frequent element in [1]
    # Expected behavior: Only one unique element exists, so return [1]
    result2 = solution.topKFrequent([1], 1)
    print(f"Test 2 - nums=[1], k=1: {result2}")

    # TEST CASE 3: Find top 2 frequent elements in [4,1,1,1,2,2,3]
    # Expected behavior: 1 appears 3 times (most frequent), 2 appears 2 times
    # So the result should be [1, 2] (the two most frequent elements)
    result3 = solution.topKFrequent([4,1,1,1,2,2,3], 2)
    print(f"Test 3 - nums=[4,1,1,1,2,2,3], k=2: {result3}")

