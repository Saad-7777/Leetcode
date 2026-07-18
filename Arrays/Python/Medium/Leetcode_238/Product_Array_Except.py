from typing import List
# Import List so type hints like List[int] work when run outside LeetCode's environment

class Solution:
    # LeetCode's required wrapper class for the solution

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method takes an array of integers, returns a new array of integers

        n = len(nums)
        # Store the length of nums so we don't call len(nums) repeatedly

        result = [1] * n
        # Create the output array, pre-filled with 1s (identity value for multiplication)

        prefix = 1
        # Running product of all elements to the LEFT of the current index; starts at 1 (nothing to the left yet)

        for i in range(n):
            # First pass: walk left to right through every index

            result[i] = prefix
            # Store the product of everything BEFORE index i (not including nums[i] itself)

            prefix *= nums[i]
            # Now fold nums[i] into the running prefix, ready for the next index

        suffix = 1
        # Running product of all elements to the RIGHT of the current index; starts at 1 (nothing to the right yet)

        for i in range(n - 1, -1, -1):
            # Second pass: walk right to left through every index (from n-1 down to 0)

            result[i] *= suffix
            # Multiply the existing left-product in result[i] by everything to the RIGHT of i

            suffix *= nums[i]
            # Now fold nums[i] into the running suffix, ready for the next (leftward) index

        return result
        # Return the fully combined array: left product × right product for every index


if __name__ == "__main__":
    # Only runs when this file is executed directly (not when imported elsewhere)

    sol = Solution()
    # Create an instance of Solution so we can call its method

    # Test case 1
    nums1 = [1, 2, 4, 6]
    # A basic array with no zeros or negatives

    print(sol.productExceptSelf(nums1))  # Expected: [48, 24, 12, 8]
    # Call the method and print the result, with the expected output noted for comparison

    # Test case 2 - contains a zero
    nums2 = [-1, 0, 1, 2, 3]
    # Includes a single zero and a negative number, to test zero-handling

    print(sol.productExceptSelf(nums2))  # Expected: [0, -6, 0, 0, 0]
    # Only the index WHERE the zero itself sits gets a non-zero product; every other index becomes 0

    # Test case 3 - two zeros (every output should be 0)
    nums3 = [0, 4, 0]
    # Two zeros present — every output index still "sees" at least one zero when excluding itself

    print(sol.productExceptSelf(nums3))  # Expected: [0, 0, 0]
    # Confirms the algorithm handles multiple