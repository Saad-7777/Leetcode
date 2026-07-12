from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group a list of strings into anagrams.

        Uses a 26-count signature (for lowercase a-z) as a hashable key.
        """
        res = defaultdict(list)

        for s in strs:
            # Create a frequency count key for the word
            count = [0] * 26  # Assuming only lowercase letters
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)

        # Return list of groups
        return list(res.values())


if __name__ == "__main__":
    # simple demonstration
    example = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(example))
