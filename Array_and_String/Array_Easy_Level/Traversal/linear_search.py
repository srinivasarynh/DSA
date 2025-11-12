
# Problem: Linear Search
# Custom Problem: https://www.geeksforgeeks.org/linear-search/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an array of integers 'arr' and an integer 'target',
implement a function to find the index of the target element using Linear Search.

If the element is found, return its index.
If not found, return -1.

Example 1:
Input: arr = [2, 4, 6, 8, 10], target = 8
Output: 3

Example 2:
Input: arr = [5, 1, 9, 3], target = 7
Output: -1

Constraints:
- 1 <= len(arr) <= 10^5
- -10^9 <= arr[i], target <= 10^9
"""


class Solution:
    def linearSearch(self, arr, target):
        """
        Perform a linear search to find the target element.
        Return index if found, else -1.
        """
        # 🧠 TODO: Write your code here
        if len(arr) == 0:
            return -1

        for idx in range(len(arr)):
            if arr[idx] == target:
                return idx

        return -1


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        {"input": {"arr": [2, 4, 6, 8, 10], "target": 8}, "expected": 3},
        {"input": {"arr": [5, 1, 9, 3], "target": 7}, "expected": -1},
        {"input": {"arr": [1], "target": 1}, "expected": 0},
        {"input": {"arr": [], "target": 5}, "expected": -1},
        {"input": {"arr": [10, 20, 30, 40], "target": 40}, "expected": 3},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.linearSearch(**t["input"])
        print(
            f"Test {i}: arr={t['input']['arr']}, target={t['input']['target']} "
            f"=> result={result}, expected={t['expected']}, "
            f"{'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
