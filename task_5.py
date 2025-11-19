def mod_number(a: int, b: int) -> int:
    '''
    Calculate the remainder of division of two natural numbers using recursion.

    Args:
        a (int): Dividend - natural number
        b (int): Divisor - natural number

    Returns:
        int: Remainder of a divided by b

    Raises:
        ValueError: If either a or b is not a natural number
    '''
    if a < b:
        return a
    return mod_number(a - b, b)


a = int(input())
b = int(input())
result = mod_number(a, b)
print(result)