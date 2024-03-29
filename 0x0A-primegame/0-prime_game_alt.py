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
    for n in range(len(nums)):
        if nums[n] % num == 0:
            nums.pop(n)
    
    return nums

def isWinner(x, nums):
    """ Plays the prime game between Ben and Mira and returns the winner
    """
    
    if x < 1:
        return None

    ben = 0
    maria = 0

    for i in range(x):
        if len(nums) == 0:
            break

        prime = 0
        for n in nums:
            if is_prime(n):
                prime = n
                break

        if prime == 0:
            break

        if i % 2 == 0:
            ben += 1
        else:
            maria += 1

        nums = filter_multiples(prime, nums)

    if ben == maria:
        return None
    return "Maria" if maria > ben else "Ben"



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
