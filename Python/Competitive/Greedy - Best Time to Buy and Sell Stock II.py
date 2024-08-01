class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curStock = 0
        ans = 0
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                ans += curStock + prices[i]
                curStock = 0
            elif prices[i] < prices[i+1] and curStock == 0:
                curStock = prices[i]
        return ans
    
print(Solution.maxProfit(list(map(int,input().split()))))