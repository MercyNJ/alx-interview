#!/usr/bin/python3
"""
Module for Prime Game Solution.
"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_round(highest_number):
    """Simulate one round of the game."""
    remaining_numbers = list(range(2, highest_number + 1))  # Start from 2, as 1 is not prime
    current_player = "Maria"

    while remaining_numbers:
        prime = None
        for num in remaining_numbers:
            if is_prime(num):
                prime = num
                break
        if prime is None:
            break

        remaining_numbers = [num for num in remaining_numbers if num % prime != 0]
        current_player = "Ben" if current_player == "Maria" else "Maria"

    return "Maria" if current_player == "Ben" else "Ben"  # Adjusted to return the last player who made a move


def isWinner(x, nums):
    """Determine the winner of the game."""
    maria_wins, ben_wins = 0, 0

    for highest_number in nums:
        winner = play_round(highest_number)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
