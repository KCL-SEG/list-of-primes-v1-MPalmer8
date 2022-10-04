"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def numIsPrime(n):
    for num in range(2,int(math.sqrt(n))+1):
        if n%num == 0:
            return False
    return True


def primes(number_of_primes):
    list = []
    num = 2
    while len(list) < number_of_primes:
        if numIsPrime:
            list.append(num)
        num += 1
    return list


    print(primes(6))
