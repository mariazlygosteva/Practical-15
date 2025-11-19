def progress(a1: float, r: float, n: int) -> float:
    '''
    Calculate the n-th term of an arithmetic progression using recursion.

    Args:
        a1 (float): First term of the progression
        r (float): Common difference of the progression
        n (int): Term number (natural number)

    Returns:
        float: The n-th term of the arithmetic progression

    Raises:
        ValueError: If n is not a natural number (n <= 0)
    '''
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)


a1 = float(input())
r = float(input())
n = int(input())
result = progress(a1, r, n)
print(result)