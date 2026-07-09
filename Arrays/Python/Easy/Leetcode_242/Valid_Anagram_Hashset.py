from typing import List


class Solution:
    def is_Anagram(self, s:str, t:str) -> bool:
        # Check if the lengths of the strings are different
        if len(s) != len(t):
            return False

        count = {}
#
        for char in s:
            #checks if the character is already in the count dictionary, if not it initializes it to 0 and then increments it by 1
            count[char] = count.get(char, 0) + 1

        for char in t:
            #checks if the character is not in the count dictionary or if its count is 0,
            # it means that t has a character that s does not have or has more occurrences of that character than s,
            # so it returns False.Otherwise, it decrements the count of that character in the count dictionary.
            if char not in count or  count[char] == 0:
                return False
            #decrements from the count dictionary for each character in t,
            #effectively "using up" the characters from s as they are matched with characters in t.
            count[char] -= 1

        return True


if __name__ == '__main__':
    print(Solution().is_Anagram(s="abcdef", t="bcd"))
    print(Solution().is_Anagram(s="racecar", t="acarrce"))




#use of get in this code, so that it does return key error



