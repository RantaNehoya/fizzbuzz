"""
fizzbuzz
"""


def fizzbuzz(x: int) -> str:
    """Returns fizz if arg is divisible by 3, buzz if arg is divisible by 5 and fizzbuzz if divisible by 3 and 5.

    Args:
        x (int): integer input

    Returns:
        str: fizz, buzz, or fizzbuzz
    """

    if x % 3 == 0:
        return "fizz"

    if x % 5 == 0:
        return "buzz"

    if (x % 3 == 0) and (x % 5 == 0):
        return "fizzbuzz"

    return str(x)


user_input = int(input("Enter a number: "))

print(fizzbuzz(user_input))
