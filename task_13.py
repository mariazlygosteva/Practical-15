def odd_list(a: list, n: int) -> list:
    '''
    Extract even numbers from a list of integers using recursion.

    Args:
        a (list): List of integer elements
        n (int): Number of elements in the list

    Returns:
        list: List containing only the even numbers from the input list

    Raises:
        ValueError: If n does not match the actual length of the list
    '''
    if n == 0:
        return []
    result = odd_list(a[1:], n - 1)
    if a[0] % 2 == 0:
        return [a[0]] + result
    return result


a = list(map(int, input().split()))
n = len(a)
result = odd_list(a, n)
print(result)