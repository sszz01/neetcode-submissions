class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])

        # return profit

        # O(n^2) solution

        # hashmap = dict()

        # for i in range(1, len(prices)):
        #     hashmap[prices[i-1]] = max(prices[i:len(prices)])

        # for i, j in hashmap.items():
        #     max_profit = j - i
        #     if max_profit > profit:
        #         profit = max_profit

        # return profit

        ## my own solution (also o(n^2))

        l,r = 0,1
        while l < len(prices):
            buy = prices[l]
            while r < len(prices):
                sell = prices[r]
                profit = max(profit, sell - buy)
                r += 1
            l += 1
            r = l + 1

        return profit
