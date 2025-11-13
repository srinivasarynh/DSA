# Problem: 387. First Unique Character in string
# LeetCode: https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Your code here
        freq_dict = dict()
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1

        for idx, char in enumerate(s):
            if freq_dict[char] == 1:
                return idx

        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ("leetcode",), "expected": 0},
        {"input": ("loveleetcode",), "expected": 2},
        {"input": ("aabb",), "expected": -1},
        {"input": ("",), "expected": -1},
        {"input": ("z",), "expected": 0},
        {"input": ("aabbccddeeffg",), "expected": 12},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.firstUniqChar(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}"
        )
