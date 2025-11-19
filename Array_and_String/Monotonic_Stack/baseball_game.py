# Problem: 682. Baseball Game
# LeetCode: https://leetcode.com/problems/baseball-game/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (operations, expected_output)
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1"], 1),
        (["10", "D", "D", "D"], 10 + 20 + 40 + 80),  # exponential doubling
        (["3", "C"], 0),                           # all removed
        (["1", "2", "+"], 3),
        (["1", "2", "3", "+"], 1 + 2 + 3 + 5),
        (["-3", "D", "+", "C"], -3*2 + (-6 + -3)),   # check negatives + cancel
        (["9", "C", "9", "C", "9"], 9),               # repeated cancel
        (["7", "4", "C", "D", "9", "+", "+"], 7 + 8 + 9 + 17 + 26),
    ]

    for i, (ops, expected) in enumerate(tests, 1):
        result = sol.calPoints(ops.copy())
        print(f"Test {i}: ops={ops}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
