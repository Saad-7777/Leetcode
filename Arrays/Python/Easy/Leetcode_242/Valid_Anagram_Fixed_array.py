from typing import List

class Solution:
    def is_Anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1


        return all(c == 0 for c in count)



if __name__ == '__main__':
    print(Solution().is_Anagram(s="abc", t="abc"))
    print(Solution().is_Anagram(s="abc", t="ac"))

#understand it later
