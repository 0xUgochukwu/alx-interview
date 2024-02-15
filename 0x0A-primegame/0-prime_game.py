#!/usr/bin/python3
""" ALX Interview - Prime Game
"""


def is_prime(num):
    """ Calculates if a given number is a prime number
    """
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def filter_multiples(num, nums):
    """ Filters out a number and it's multiples from a list of numbers
    """
    # to_remove = []
    # for n in range(len(nums)):
    #     if nums[n] % num == 0:
    #         to_remove.append(nums[n])
    # for n in to_remove:
    #     nums.remove(n)
    # return nums
    return list(filter(lambda x: x % num != 0, nums))


def isWinner(x, nums):
    if x < 1:
        return None

    scores = {"Maria": 0, "Ben": 0}
    for n in nums:
        numbers = list(range(1, n + 1))
        turn = "Maria"
        while True:
            primes = [i for i in numbers if is_prime(i)]
            if not primes:
                scores[turn] += 1
                break
            prime = min(primes)
            numbers = filter_multiples(prime, numbers)
            turn = "Ben" if turn == "Maria" else "Maria"

    if scores["Maria"] == scores["Ben"]:
        return None
    return "Maria" if scores["Maria"] > scores["Ben"] else "Ben"

# def isWinner(x, nums):
#     """ Plays the prime game between Ben and Mira and returns the winner
#     """
#     if x < 1:
#         return None

#     players = {"Ben": 0, "Maria": 0}
#     player = "Maria"

#     for i in range(x):
#         if len(nums) == 0:
#             break

#         num_range = range(1, nums + 1)
#         for i in num_range:
#             if is_prime(i):
#                 num_range = filter_multiples(i, num_range)
#                 players[player] += 1
#                 player = "Ben" if player == "Maria" else "Maria"
#             players[player] += 1

#         player = "Maria"

#     if players["Ben"] == players["Maria"]:
#         return None
#     return max(players, key=players.get)