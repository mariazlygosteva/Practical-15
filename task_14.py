def numbers(x: int) -> None:
    '''
    Print the digits of a natural number in reverse order, one per line.

    Args:
        x (int): Natural number to process

    Returns:
        None: This function does not return anything, it only prints

    Raises:
        ValueError: If x is not a natural number (x <= 0)
    '''
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


x = int(input())
print()
numbers(x)