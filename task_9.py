def combin(n: int, k: int) -> int:
    '''
    Calculate the binomial coefficient (combination) using recursion.

    Args:
        n (int): Total number of items
        k (int): Number of items to choose

    Returns:
        int: Number of ways to choose k items from n items

    Raises:
        ValueError: If k is negative or greater than n
    '''
    if k == 0 or k == n:
        return 1
    return combin(n - 1, k - 1) + combin(n - 1, k)


n = int(input())
k = int(input())
result = combin(n, k)
print(result)