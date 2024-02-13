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
    remaining_numbers = list(range(1, highest_number + 1))
    current_player = "Maria"

    for _ in range(len(remaining_numbers)):
        prime_numbers = [num for num in remaining_numbers if is_prime(num)]
        if not prime_numbers:
            break  # Exit the loop if there are no prime numbers left
        for prime in prime_numbers:
            # Remove multiples of prime numbers chosen by the current player
            remaining_numbers = \
                    [num for num in remaining_numbers if num % prime != 0]
            # Append the prime number itself to the list of remaining numbers
            remaining_numbers.append(prime)

        current_player = "Ben" if current_player == "Maria" else "Maria"

    return "Maria" if current_player == "Ben" else "Ben"


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
