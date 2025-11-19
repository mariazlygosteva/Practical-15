def ind_maxlist(a: list) -> int:
    '''
    Find the index of the maximum element in a list of integers using recursion.

    Args:
        a (list): List of integer elements

    Returns:
        int: Index of the maximum element in the list

    Raises:
        ValueError: If the list is empty
    '''
    if len(a) == 1:
        return 0
    max_index = ind_maxlist(a[1:]) + 1
    return 0 if a[0] >= a[max_index] else max_index


a = list(map(int, input().split()))
result = ind_maxlist(a)
print(result)