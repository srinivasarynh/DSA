# Problem: 1047. Remove all adjacent duplicates in string
# LeetCode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("aabbcc", ""),
        ("aabcca", "bca"),
        ("aaaa", ""),
        ("abc", "abc"),
        ("a", "a"),
        ("", ""),
        ("abba", ""),          # fully removes
        ("abbbaa", "aba"),     # multiple collapse waves
        ("abbcccbdaaa", "ad"),  # tricky nested removals
        ("zyzzya", "za"),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        result = sol.removeDuplicates(s)
        print(f"Test {i}: s='{s}'")
        print(f"  Expected: '{expected}', Got: '{result}'")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
