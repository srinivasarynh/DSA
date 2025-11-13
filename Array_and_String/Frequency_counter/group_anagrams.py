# Problem: 49. Group Anagrams
# LeetCode: https://leetcode.com/problems/group-anagrams/description/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Your code here
        result = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            result[key].append(word)

        return list(result.values())


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": (["eat", "tea", "tan", "ate", "nat", "bat"],), "expected": [
            ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]},
        {"input": ([""],), "expected": [[""]]},
        {"input": (["a"],), "expected": [["a"]]},
        {"input": (["abc", "bca", "cab", "xyz", "zyx"],), "expected": [
            ["abc", "bca", "cab"], ["xyz", "zyx"]]},
        {"input": ([],), "expected": []},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.groupAnagrams(*t["input"])
        # Normalize output by sorting inner and outer lists before comparison
        def normalize(lst): return sorted([sorted(group) for group in lst])
        result_norm = normalize(result)
        expected_norm = normalize(t['expected'])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result_norm==expected_norm else '❌ FAIL'}"
        )
