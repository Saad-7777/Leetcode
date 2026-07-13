# Import the List type from typing module to provide type hints for function parameters
from typing import List

# Define the Solution class that contains the topKFrequent method
class Solution:
    # Method to find the K most frequent elements in the given list of numbers
    # Parameters:
    #   - nums: List of integers to analyze
    #   - k: The number of most frequent elements to return
    # Returns: List of integers representing the k most frequent elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty dictionary to store the frequency count of each number
        # Key: the number itself, Value: how many times it appears in nums
        count = {}

        # Create a frequency bucket list where index represents frequency and value stores numbers with that frequency
        # Length is len(nums) + 1 because a number can appear at most len(nums) times
        # Each bucket is initialized as an empty list to hold numbers with that frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # First loop: Count the frequency of each number in nums
        for num in nums:
            # Use the get() method to safely retrieve the current count (default 0 if not found) and add 1
            # This builds a frequency map for all unique numbers in the input
            count[num] = count.get(num, 0) + 1

        # Second loop: Populate the frequency buckets using the count dictionary
        for num, cnt in count.items():
            # cnt is the frequency count, so we append the number to the bucket at index cnt
            # This creates a mapping: freq[frequency] = [all numbers with that frequency]
            freq[cnt].append(num)

        # Initialize an empty list to store the result (the k most frequent elements)
        result = []

        # Third loop: Traverse the frequency buckets from highest frequency to lowest
        # Start from len(freq) - 1 (highest possible frequency) and go down to 1
        # Step -1 means we iterate backwards through the indices
        for i in range(len(freq) - 1, 0, -1):
            # Inner loop: For each number in the current frequency bucket
            for num in freq[i]:
                # Append the number to the result list
                result.append(num)
                # Check if we have already collected k elements
                if len(result) == k:
                    # If we have k elements, return the result immediately (early exit for efficiency)
                    return result

        # Return the result list (in case we've collected all elements and they're less than k)
        # This handles edge cases where there are fewer than k unique elements
        return result


# This section only runs when the script is executed directly (not when imported as a module)
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
