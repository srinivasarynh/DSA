
# Problem: 844. Backspace String Compare
# LeetCode: https://leetcode.com/problems/backspace-string-compare/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given two strings s and t, return True if they are equal when both are typed into
empty text editors. '#' means a backspace character.

Note:
- After backspacing an empty text, it remains empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: True
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: True
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: False
Explanation: s becomes "c" while t becomes "b".

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

Follow-up:
Can you solve it in O(n) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Compare two strings after simulating typing with backspaces.
        Returns True if both result in the same string, otherwise False.
        """
        # 🧠 TODO: Implement logic here

        def build(st: str) -> str:
            stack = []
            for ch in st:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # ✅ Basic cases
        {"input": {"s": "ab#c", "t": "ad#c"}, "expected": True},   # both -> "ac"
        {"input": {"s": "ab##", "t": "c#d#"}, "expected": True},   # both -> ""
        {"input": {"s": "a#c", "t": "b"}, "expected": False},      # "c" != "b"
        # ✅ Both empty after backspaces
        {"input": {"s": "a###", "t": "##"}, "expected": True},
        # ✅ Different length but same result
        {"input": {"s": "bxj##tw", "t": "bxo#j##tw"}, "expected": True},
        # ✅ Multiple backspaces in sequence
        {"input": {"s": "xywrrmp", "t": "xywrrmu#p"}, "expected": True},
        # ✅ Edge case: only one character
        {"input": {"s": "a", "t": "a"}, "expected": True},
        {"input": {"s": "a", "t": "b"}, "expected": False},
        # ✅ Edge case: all backspaces
        {"input": {"s": "#####", "t": "##"}, "expected": True},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.backspaceCompare(**t["input"])
        print(
            f"Test {i}: s={t['input']['s']}, t={t['input']['t']} "
            f"=> result={result}, expected={t['expected']}, "
            f"{'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
