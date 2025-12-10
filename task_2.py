def count(n: int) -> int:
    '''
    Calculate the number of digits in a natural number using recursion.

    Args:
        n: Natural number (positive integer)

    Returns:
        Number of digits in the given number
    '''
    if n < 10:
        return 1
    return 1 + count(n // 10)


def main() -> None:
    '''The main function of the program.'''
    n = int(input())
    result = count(n)
    print(result)


if __name__ == "__main__":
    main()
