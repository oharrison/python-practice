from collections import Counter

def most_duplicated_with_counter(lst):
    """
    Args:
        lst (list): A sorted list of integers

    Returns:
        int: The integer in lst that occurs most often

    Examples:
        >>> most_duplicated_with_counter([])
        >>> most_duplicated_with_counter([1])
        >>> most_duplicated_with_counter([1, 2, 2, 3])
    """
    if len(lst) == 0:
        return -1

    # ensure lst is sorted
    assert sorted(lst) == lst
    
    return Counter(lst).most_common()[0][0]

def most_duplicated_without_counter(lst):
    """
    Args:
        lst (list): A sorted list of integers

    Returns:
        int: The integer in lst that occurs most often

    Examples:
        >>> most_duplicated_without_counter([])
        >>> most_duplicated_without_counter([1])
        >>> most_duplicated_without_counter([1, 2, 2, 3])
    """
    lst_length = len(lst)

    if lst_length == 0:
        return -1

    # ensure lst is sorted
    assert sorted(lst) == lst

    current_position = 0
    current_occurence, previous_occurence = 1, 0
    most_dupped = lst[current_position]

    while current_position < lst_length:
        next_position = current_position + 1
        while next_position < lst_length and lst[current_position] == lst[next_position]:
            current_occurence += 1
            next_position += 1
            if current_occurence > previous_occurence:
                most_dupped = lst[current_position]
        current_position = next_position

    return most_dupped

if __name__ == '__main__':
    assert(most_duplicated_with_counter(list()) == -1)
    assert(most_duplicated_without_counter(list()) == -1)
    assert(most_duplicated_with_counter([1]) == 1)
    assert(most_duplicated_without_counter([1]) == 1)
    assert(most_duplicated_with_counter([1, 2]) == 1)
    assert(most_duplicated_without_counter([1, 2]) == 1)
    assert(most_duplicated_with_counter([1, 2, 2, 4,10]) == 2)
    assert(most_duplicated_without_counter([1, 2, 2, 4, 9, 9, 9, 10]) == 9)
