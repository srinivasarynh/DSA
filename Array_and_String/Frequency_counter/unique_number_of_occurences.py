
# Problem: 1207. Unique Number of Occurrences
# LeetCode: https://leetcode.com/problems/unique-number-of-occurrences/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3
"""
LeetCode Problem 1207: Unique Number of Occurrences
Difficulty: Easy
Pattern: Frequency Counter (Hash Map)

🧩 Problem Statement:
Given an array of integers `arr`, return True if the number of occurrences of each value 
in the array is unique, or False otherwise.

Constraints:
- 1 <= len(arr) <= 1000
- -1000 <= arr[i] <= 1000
"""

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Count the occurrences of each number using a hash map (Counter),
        and check if all frequency counts are unique.
        """
        # Brute force
        '''
        if not arr:
            return False

        map_counter = dict()
        for ele in arr:
            if ele not in map_counter.keys():
                map_counter[ele] = 1
            map_counter[ele] += 1

        my_arr = map_counter.values()
        return len(my_arr) == len(set(map_counter.values()))
        '''
        # Optimized
        freq_map = Counter(arr)
        occurences = list(freq_map.values())
        return len(occurences) == len(set(occurences))


# ----------------------------
# ✅ Test Cases
# ----------------------------
def run_tests():
    sol = Solution()

    test_cases = [
        # Example cases
        # frequencies: {1:3, 2:2, 3:1} -> all unique
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),              # frequencies: {1:1, 2:1} -> not unique
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),  # frequencies unique

        # Edge cases
        ([5], True),                 # single element -> one frequency
        # all same elements -> one frequency (max constraint)
        ([1000]*1000, True),
        ([1, 1, 2, 2, 3, 3], False),      # same frequencies (2 for each)
        ([1, 1, 1, 2, 2, 3], True),       # 1→3, 2→2, 3→1 -> unique
        # all unique numbers -> all frequencies 1, but same → False
        (list(range(1000)), True),
        # one duplicated, frequencies not unique
        (list(range(1000)) + [999], False),
        ([0, 0, 0, 0, 1, 1, 2], True),     # freq: {0:4, 1:2, 2:1} unique
    ]

    for idx, (arr, expected) in enumerate(test_cases, 1):
        result = sol.uniqueOccurrences(arr)
        assert result == expected, f"❌ Test {idx} failed: expected {expected}, got {result}"
        print(f"✅ Test {idx} passed")


if __name__ == "__main__":
    run_tests()
