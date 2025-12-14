import heapq
from typing import List

def max_profit_greedy(stock_prices: List[int]) -> int:
    options = []
    current_profit = 0

    for price in stock_prices:
        if len(options) >  0 and price > options[0]:
            current_profit += price - options[0]
            heapq.heappop(options)

        heapq.heappush(options, price)

    return current_profit
