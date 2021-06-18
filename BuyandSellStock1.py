# Time: O(N^2)        Space: O(1)
"""
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            curr_profit = prices[j] - prices[i]
            if curr_profit > max_profit:
                max_profit = curr_profit
    return max_profit
"""
# Time: O(N)      Space: O(1)
def maxProfit(prices):
    buy = prices[0]
    maxprofit = 0
    for i in range(1, len(prices)):
        profit = prices[i] - buy

        if profit > maxprofit:
            maxprofit = profit

        if buy > prices[i]:
            buy = prices[i]

    return maxprofit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))