from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice_opt(prices: List[float]) -> float:
    """
    O(n) space and time
    """
    curr_min_price, max_profit = float('inf'), 0.0
    first_profits = [0.0] * len(prices)

    for i, price in enumerate(prices):
        curr_min_price = min(curr_min_price, price)
        max_profit = max(price - curr_min_price, max_profit)
        first_profits[i] = max_profit

    curr_max_price = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        curr_max_price = max(curr_max_price, price)
        max_profit = max(
            max_profit,
            curr_max_price - price + first_profits[i])
    return max_profit


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """
    O(1) space and O(n) time

    Take the max profit of first transaction by selling at or before current i.
    max_profit = max(p - min[p0...pi-1])

    If we sold stock before the current day, we can buy again today.
    We dedut the current day's price from the previous buy_sell profit.
    max_leftover = max(Pi - max_profit)

    If we bought second stock before the current day i, you can sell today too.
    Doing so, we add today's price to the previous leftover profit.
    This gives us the current profit for day i with 2 transactions.
    Max profit at day i for two transactions:
    max(Pi + max_leftover)

    """
    min_price = float('inf')
    max_profit_first_sell = 0
    max_profit_left_second_buy = float('-inf')
    max_profit_second_sell = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit_first_sell = max(price - min_price, max_profit_first_sell)
        max_profit_left_second_buy = max(
            max_profit_first_sell - price,
            max_profit_left_second_buy)
        max_profit_second_sell = max(
            price + max_profit_left_second_buy,
            max_profit_second_sell)

    return max_profit_second_sell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
