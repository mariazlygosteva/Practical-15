def progress(a1: float, r: float, n: int) -> float:
    '''
    Calculate the n-th term of an arithmetic progression using recursion.

    Args:
        a1 (float): First term of the progression
        r (float): Common difference of the progression
        n (int): Term number (natural number)

    Returns:
        float: The n-th term of the arithmetic progression
    '''
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)


def main() -> None:
    '''The main function of the program.'''
    a1 = float(input())
    r = float(input())
    n = int(input())
    result = progress(a1, r, n)
    print(result)


if __name__ == "__main__":
    main()
