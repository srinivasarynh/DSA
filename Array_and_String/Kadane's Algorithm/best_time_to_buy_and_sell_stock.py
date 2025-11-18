# problem: 121. Best Time to buy and sell stock
# leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# author: srinivas
# date: 2025-11-18
# language: python3


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price-min_price)

        return max_profit
# --------------------------
# Test cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([2, 4, 1], 2),
        ([2, 1, 4], 3),
        ([3, 3, 3], 0),
        ([3], 0),              # Only one price
        ([], 0),               # No prices
        ([9, 8, 7, 1, 2], 1),
    ]

    for i, (prices, expected) in enumerate(tests, 1):
        result = sol.maxProfit(prices)
        print(f"Test {i}: prices={prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
