# Problem: 739. Daily Temperature
# LeetCode: https://leetcode.com/problems/daily-temperatures/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result

# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (temperatures, expected_output)
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 1, 0, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([60, 50, 40, 30], [0, 0, 0, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 60, 30], [0, 0, 0]),
        ([45], [0]),                 # single element
        ([], []),                    # empty
        ([70, 70, 70], [0, 0, 0]),       # no warmer days
        ([70, 80, 60, 90], [1, 2, 1, 0]),
        ([55, 38, 53, 81, 61, 93], [3, 1, 1, 2, 1, 0]),
        ([89, 62, 70, 58, 47, 47, 46, 76, 100], [8, 1, 1, 3, 3, 2, 1, 1, 0]),
    ]

    for i, (temps, expected) in enumerate(tests, 1):
        result = sol.dailyTemperatures(temps.copy())
        print(f"Test {i}: temperatures={temps}")
        print(f"  Expected: {expected}")
        print(f"  Got     : {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
