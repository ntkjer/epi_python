from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once_bf(prices: List[float]) -> float:
    max_diff = 0
    for i in range(len(prices) - 1):
        for j in range(1, len(prices) - 1):
            curr_diff = abs(prices[j] - prices[i])
            if curr_diff > max_diff:
                max_diff = curr_diff
    return max_diff


def buy_and_sell_stock_once(prices: List[float]) -> float:
    """
    max difference algorithm:
    keep track of min price and max diff
    """
    curr_min_price, max_profit = float('inf'), 0.0
    for price in prices:
        curr_profit = price - curr_min_price
        max_profit = max(curr_profit, max_profit)
        curr_min_price = min(curr_min_price, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
