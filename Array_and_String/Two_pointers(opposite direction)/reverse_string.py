# problem: 344. Reverse string
# leetcode: https://leetcode.com/problems/reverse-string/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return []

        left = 0
        right = len(s)-1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input_list, expected_list)
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        ([], []),
        (["A", "B", "C", "D"], ["D", "C", "B", "A"]),
        (["1", "2", "3", "4", "5"], ["5", "4", "3", "2", "1"]),
        (["x", "x", "x"], ["x", "x", "x"]),
        (["!", "@", "#"], ["#", "@", "!"]),
    ]

    for i, (input_list, expected) in enumerate(tests, 1):
        arr = input_list[:]  # copy to avoid mutation issues
        sol.reverseString(arr)
        print(f"Test {i}:")
        print(f" Input: {input_list}")
        print(f" Output: {arr}")
        print(f" Expected: {expected}")
        print(" Pass:", arr == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
