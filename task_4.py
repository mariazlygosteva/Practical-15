def sum_progress(a1: float, r: float, n: int) -> float:
    '''
    Calculate the sum of the first n terms of an arithmetic progression using recursion.

    Args:
        a1 (float): First term of the progression
        r (float): Common difference of the progression
        n (int): Number of terms to sum (natural number)

    Returns:
        float: Sum of the first n terms of the arithmetic progression

    Raises:
        ValueError: If n is not a natural number (n <= 0)
    '''
    if n == 1:
        return a1
    return (a1 + (n - 1) * r) + sum_progress(a1, r, n - 1)


a1 = float(input())
r = float(input())
n = int(input())
result = sum_progress(a1, r, n)
print(result)