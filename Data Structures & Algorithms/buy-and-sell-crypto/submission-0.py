class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        least=prices[0]
        profit=0
        for num in prices:
            if num<least:
                least=num
                continue
            elif num>least:
                profit=num-least
            maxprofit=max(maxprofit, profit)
        return maxprofit