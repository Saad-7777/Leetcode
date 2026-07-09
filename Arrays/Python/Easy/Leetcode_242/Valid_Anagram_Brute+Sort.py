from typing import List

class Solution:
    def is_Anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(Solution().is_Anagram(s="abc", t="abc"))






# Time Complexity O(n log n), Space Complexity O(n)