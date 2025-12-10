def fib(k: int) -> int:
    '''
    Calculate the k-th term of the Fibonacci sequence using recursion.

    Args:
        k (int): Index of the Fibonacci term (non-negative integer)

    Returns:
        int: The k-th Fibonacci number
    '''
    if k <= 1:
        return k
    return fib(k - 1) + fib(k - 2)


def main() -> None:
    '''The main function of the program.'''
    k = int(input())
    result = fib(k)
    print(result)


if __name__ == "__main__":
    main()
