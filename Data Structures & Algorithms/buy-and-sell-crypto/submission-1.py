class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = prices[j] - prices[i]
                if max_profit > profit:
                    profit = max_profit

        return profit
