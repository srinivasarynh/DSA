# Problem: 1441. Build an array with stack operations
# LeetCode: https://leetcode.com/problems/build-an-array-with-stack-operations/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        stack = []
        cur_num = 1

        for t in target:
            while cur_num < t:
                stack.append("Push")
                stack.append("Pop")
                cur_num += 1
            stack.append("Push")
            cur_num += 1

        return stack
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (target, n, expected_output)
        ([1, 3], 3, ["Push", "Push", "Pop", "Push"]),
        ([1, 2, 3], 3, ["Push", "Push", "Push"]),
        ([2, 3, 4], 4, ["Push", "Pop", "Push", "Push", "Push"]),
        ([1], 1, ["Push"]),
        ([1], 5, ["Push"]),
        ([3], 5, ["Push", "Pop", "Push", "Pop", "Push"]),
        ([2], 2, ["Push", "Pop", "Push"]),
        ([4], 4, ["Push", "Pop", "Push", "Pop", "Push", "Pop", "Push"]),
        ([1, 2], 4, ["Push", "Push"]),
        ([2, 4], 5, ["Push", "Pop", "Push", "Push", "Pop", "Push"]),
    ]

    for i, (target, n, expected) in enumerate(tests, 1):
        result = sol.buildArray(target, n)
        print(f"Test {i}: target={target}, n={n}")
        print(f"  Expected: {expected}")
        print(f"  Got     : {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
