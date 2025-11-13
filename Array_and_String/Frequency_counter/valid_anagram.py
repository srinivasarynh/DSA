# Problem: 242. Valid Anagram
# LeetCode: https://leetcode.com/problems/valid-anagram/description/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Your code here
        # Brute force
        """
        s_dict = dict()
        t_dict = dict()

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        return s_dict == t_dict
        """

        # Optimized using Counter
        # return Counter(s) == Counter(t)

        # more Optimized (one pass)
        s_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char not in s_dict:
                return False
            s_dict[char] -= 1
            if s_dict[char] < 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ("anagram", "nagaram"), "expected": True},
        {"input": ("rat", "car"), "expected": False},
        {"input": ("", ""), "expected": True},
        {"input": ("a", "b"), "expected": False},
        {"input": ("aacc", "ccac"), "expected": False},
        {"input": ("åßç", "çßå"), "expected": True},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.isAnagram(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}"
        )
