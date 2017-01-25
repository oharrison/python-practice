def next_server_number(server_numbers):
    if server_numbers:
        len_server_numbers = len(server_numbers)
        if len_server_numbers == 1:
            return 2 if server_numbers[0] == 1 else 1
        sorted_server_numbers = sorted(server_numbers)
        for i, server_number in enumerate(sorted_server_numbers):
            if i == len_server_numbers - 1:
                return server_number + 1
            elif i + 1 != server_number:
                return i + 1
    return 1

if __name__ == '__main__':
    assert next_server_number([5, 3, 1]) == 2
    assert next_server_number([5, 4, 1, 2]) == 3
    assert next_server_number([3, 2, 1]) == 4
    assert next_server_number([2, 3]) == 1
    assert next_server_number([2]) == 1
    assert next_server_number([]) == 1
    print('All tests passed.')
