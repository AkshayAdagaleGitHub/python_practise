# Smallest Substring of All Characters
from traceback import print_tb
from typing import List

import BusiestTimeInMall
import buy_and_sell_stock
from deletion_distance import deletion_distance


def get_shortest_unique_substring(arr: List[str], s: str) -> str:
     count_map = {char: 0 for char in s}

     head_index = 0
     unique_count = 0
     result = ""

     for tail_index in range(len(s)):
         tail_char = s[tail_index]
         if tail_char in count_map:
             if count_map[tail_char] == 0:
                 unique_count += 1
             count_map[tail_char] += 1
         while unique_count == len(arr):
             temp_length = tail_index - head_index + 1
             if temp_length == len(arr):
                 return s[head_index:tail_index +1]
             if result == "" or temp_length < len(result):
                 result = s[head_index:tail_index + 1]

             head_char = s[head_index]
             if head_char in count_map:
                 count_map[head_char] -= 1
                 if count_map[head_char] == 0:
                     unique_count -= 1
             head_index += 1

     return result

def __main__():

    # Buy And Sell Stock
    stock_prices = [7, 1, 5, 3, 6, 4]
    print(buy_and_sell_stock.max_profit_greedy(stock_prices))
    # output: 7 (Buy on day 2 at 1, sell on day 3 at 5, buy on day 4 at 3, and sell on day 5 at 6)
    stock_prices = [1, 2, 3, 4, 5]
    print(buy_and_sell_stock.max_profit_greedy(stock_prices))
    # output: 4 (Buy on day 1 at 1 and sell on day 5 at 5)
    stock_prices = [7, 6, 4, 3, 1]
    print(buy_and_sell_stock.max_profit_greedy(stock_prices))
    # output: 0 (No transaction is done, i.e., max profit = 0)
    stock_prices = [1, 10, 2, 3]
    print(buy_and_sell_stock.max_profit_greedy(stock_prices))
    # output: 10 (Buy on day 1 at 1 and sell on day 2 at 10)

    # // BusiestTimeInMall
    # BusiestTimeInMall.find_busiest_time([[1487799425, 14, 1],
    #                      [1487799425, 4, 1],
    #                      [1487799425, 2, 1],
    #                      [1487800378, 10, 1],
    #                      [1487801478, 18, 1],
    #                      [1487901013, 1, 1],
    #                      [1487901211, 7, 1],
    #                      [1487901211, 7, 1]])
    # Deletion distance
    # str1 = "frog"
    # str2 = "dog"
    # print(deletion_distance(str1, str2))

    # get_shortest_unique_substring
    # arr = ["x", "y", "z"]
    # s="xyyzyzyx"
    # print(get_shortest_unique_substring(arr, s))


if __name__ == '__main__':
    __main__()