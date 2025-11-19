def count(a: int, b: int) -> int:
    '''
    Count the number of squares that can be cut from a rectangle using recursion.

    Args:
        a (int): Length of the rectangle (natural number)
        b (int): Width of the rectangle (natural number)

    Returns:
        int: Number of squares that can be cut from the rectangle

    Raises:
        ValueError: If either a or b is not a natural number
    '''
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a
    return 1 + count(a - b, b)


a = int(input())
b = int(input())
result = count(a, b)
print(result)