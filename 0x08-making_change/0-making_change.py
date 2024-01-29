#!/usr/bin/python3
"""
Calculate the minimum number of coins needed to make up a given total.
"""


def makeChange(coins, total):
    """
    Calculate the min number of coins needed to make up a given total.

    Parameters:
        coins (list): List of coin denominations.
        total (int): Target total amount.

    Returns:
        int: Min n0 of coins needed to make uptotal, or -1 if not possible.
    """

    required_coins = 0
    remainder = 0

    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        while (total >= coin):
            whole_coins = total // coin
            remainder = total % coin
            required_coins += whole_coins
            total = remainder
    if total == 0:
        return required_coins
    else:
        return -1
