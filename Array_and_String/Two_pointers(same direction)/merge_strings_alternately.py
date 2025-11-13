
# Problem: 1768. Merge Strings Alternately
# LeetCode: https://leetcode.com/problems/merge-strings-alternately/description/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3

"""
LeetCode Problem 1768: Merge Strings Alternately
Difficulty: Easy

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Constraints:
1 <= len(word1), len(word2) <= 100
word1 and word2 consist of lowercase English letters.
"""

from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately. Append the remaining part of the longer string at the end.
        """
        if not word1:
            return word2

        if not word2:
            return word1

        len1, len2 = len(word1), len(word2)
        i, j = 0, 0
        merged = []

        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
            j += 1

        if i < len1:
            merged.append(word1[i:])

        if j < len2:
            merged.append(word2[j:])

        return "".join(merged)
# ----------------------------
# Test Cases
# ----------------------------


def run_tests():
    sol = Solution()

    test_cases = [
        # Example cases
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),

        # Edge cases
        ("a", "b", "ab"),                 # both single character
        ("z", "xyz", "zx yz" .replace(" ", "")),  # one much shorter
        ("hello", "world", "hweolrllod"),  # equal length
        ("x", "abcde", "xabcde"),         # first string very short
        ("abcde", "x", "axbcde"),         # second string very short
        # max constraint same length
        ("a"*100, "b"*100, "".join(a+b for a, b in zip("a"*100, "b"*100))),
        # uneven long strings
        ("a"*100, "b"*50, "".join(a+b for a, b in zip("a"*50, "b"*50)) + "a"*50),
    ]

    for idx, (w1, w2, expected) in enumerate(test_cases, 1):
        result = sol.mergeAlternately(w1, w2)
        assert result == expected, f"❌ Test {idx} failed: expected {expected}, got {result}"
        print(f"✅ Test {idx} passed: {result}")


if __name__ == "__main__":
    run_tests()
