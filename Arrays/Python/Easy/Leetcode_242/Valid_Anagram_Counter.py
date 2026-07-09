from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    print(Solution().isAnagram(s="abc", t="abc"))
    print(Solution().isAnagram(s="abc", t="aec"))

    print(Solution().isAnagram(s="abc", t="abcf"))



# Time Complexity O(n), Space Complexity O(1)

