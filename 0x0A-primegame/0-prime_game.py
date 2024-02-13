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


def precompute_primes(max_num):
    """Precompute prime numbers up to max_num."""
    primes = []
    for num in range(2, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def determine_winner(primes, n):
    """Determine the winner based on available prime numbers."""
    available_primes = sum(prime <= n for prime in primes)
    return "Maria" if available_primes % 2 else "Ben"


def isWinner(x, nums):
    """Determine the winner of the game."""
    if max(nums) > 10000 or x > 10000:
        raise ValueError("Input values exceed maximum limit.")

    players_wins = {"Maria": 0, "Ben": 0}
    all_primes = precompute_primes(max(nums))

    for n in nums:
        winner = determine_winner(all_primes, n)
        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"
    else:
        return None
