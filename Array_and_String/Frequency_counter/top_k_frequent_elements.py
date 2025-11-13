# Problem: 347. Top K Frequent Elements
# LeetCode: https://leetcode.com/problems/top-k-frequent-elements/description/?utm_source=chatgpt.com
# Author: srinivas
# Date: 2025-11-13
# Language: Python3


"""
LeetCode Problem 347: Top K Frequent Elements
Difficulty: Medium
Pattern: Frequency Counter + Heap / Bucket Sort

🧩 Problem Statement:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
You may return the answer in any order.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Follow-up: 
Can you solve it in O(n) time complexity?
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 1: Hash Map + Min Heap
        - Count the frequency of each number using Counter.
        - Use a min-heap of size k to store the top k frequent elements.
        - Time: O(n log k), Space: O(n)
        """
        # Brute force
        """
        freq = dict()
        for ele in nums:
            if ele not in freq.keys():
                freq[ele] = 1
            freq[ele] += 1
        """
        # Optimized
        """
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [value for count, value in heap]
        """
        freq = Counter(nums)
        return [idx for idx, count in freq.most_common(k)]

# ----------------------------
# ✅ Test Cases
# ----------------------------


def run_tests():
    sol = Solution()

    test_cases = [
        # Example cases
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),

        # Edge cases
        # one clear dominant element
        ([4, 4, 4, 6, 6, 7, 7, 7, 7], 1, [7]),
        ([4, 4, 4, 6, 6, 7, 7, 7, 7], 2, [7, 4]),        # top 2 frequent
        # all appear once, any top k valid
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [1, 2, 3]),
        # 3 appears 4 times, 5 appears 3 times
        ([5, 5, 5, 4, 4, 3, 3, 3, 3], 2, [3, 5]),
        # top 3 in descending frequency
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3, [4, 3, 2]),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5, [
         1, 2, 3, 4, 5]),  # all equal frequency
        ([10000]*10000 + [5]*9999 + [1], 1, [10000]),  # large case, one dominant
        ([x % 10 for x in range(1000)], 10, list(
            range(10))),  # uniform distribution
    ]

    for idx, (nums, k, expected) in enumerate(test_cases, 1):
        result = sol.topKFrequent(nums, k)
        # Order can vary, so compare as sets
        assert set(result) == set(
            expected), f"❌ Test {idx} failed: expected {expected}, got {result}"
        print(f"✅ Test {idx} passed")


if __name__ == "__main__":
    run_tests()
