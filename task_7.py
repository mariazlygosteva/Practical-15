def node(a: int, b: int) -> int:
    '''
    Calculate the greatest common divisor of two natural numbers using recursion.

    Args:
        a (int): First natural number
        b (int): Second natural number

    Returns:
        int: Greatest common divisor of a and b
    '''
    if b == 0:
        return a
    return node(b, a % b)


def main() -> None:
    '''The main function of the program.'''
    a = int(input())
    b = int(input())
    result = node(a, b)
    print(result)


if __name__ == "__main__":
    main()
